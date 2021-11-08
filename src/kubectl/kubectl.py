from typing import AnyStr, Dict, Union
from kubernetes import client, config

import base64

class Kubectl:
    def __init__(self) -> None:
        """
        Initialize kubernetes client
        """
        self.__api_client = None

    @property
    def __api(self):
        """
        Init connection to kubectl
        """
        if not self.__api_client:
            config.load_kube_config()
            self.__api_client = client.CoreV1Api()

        return self.__api_client

    def get_secret(self, secret: AnyStr, namespace: AnyStr = "default") -> Union[Dict, None]:
        """
        Get secret from kubernetes cluster
        Args:
            secret: Secret name
            namespace (Optional):  Namespace where to search for secret
                      (Default: default)

        Returns:
            Secret reference
        """
        secret = self.__api.read_namespaced_secret(secret, namespace)
        secret_data = {}
        for k,v in secret.data.items():
            secret_data[k] = base64.b64decode(v).decode('utf-8')

        return secret_data

    def get_service(self, name: AnyStr, namespace: AnyStr = "default") -> Union[Dict, None]:
        """
        Get secret from kubernetes cluster
        Args:
            name: service name
            namespace (Optional):  Namespace where to search for secret
                      (Default: default)

        Returns:
            Service reference
        """
        all_services = self.__api.list_namespaced_service(namespace)
        requested_service = None
        for item in all_services.items:
            if name == item.metadata.name:
                requested_service = item
            
        if not requested_service:
            raise IOError(f"service not found")

        return requested_service

if __name__ == "__main__":
    k = Kubectl()
    print(k.get_secret("postgresdb-secret", namespace="reservi"))

