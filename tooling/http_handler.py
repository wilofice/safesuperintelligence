import requests


class HttpHandler:
    def __init__(self, base_url):
        """
        Initializes the HttpHandler with a base URL.
        """
        self.base_url = base_url

    def get(self, endpoint, params=None, headers=None):
        """
        Sends a GET request.

        :param endpoint: The API endpoint to hit.
        :param params: Query parameters to include in the GET request.
        :param headers: Optional headers to include in the request.
        :return: The response object.
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"GET request failed: {e}")
            return None

    def post(self, endpoint, data=None, json=None, headers=None):
        """
        Sends a POST request.

        :param endpoint: The API endpoint to hit.
        :param data: Data to include in the POST request body.
        :param json: JSON data to include in the POST request body.
        :param headers: Optional headers to include in the request.
        :return: The response object.
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.post(url, data=data, json=json, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"POST request failed: {e}")
            return None

    def put(self, endpoint, data=None, json=None, headers=None):
        """
        Sends a PUT request.

        :param endpoint: The API endpoint to hit.
        :param data: Data to include in the PUT request body.
        :param json: JSON data to include in the PUT request body.
        :param headers: Optional headers to include in the request.
        :return: The response object.
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.put(url, data=data, json=json, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"PUT request failed: {e}")
            return None

    def delete(self, endpoint, headers=None):
        """
        Sends a DELETE request.

        :param endpoint: The API endpoint to hit.
        :param headers: Optional headers to include in the request.
        :return: The response object.
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.delete(url, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"DELETE request failed: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Create an instance of the HttpHandler class with the base URL
    api_client = HttpHandler("http://localhost:8080")

    # Example GET request
    get_response = api_client.get("/api/goals")
    if get_response:
        print("GET response:", get_response.json())

    # Example POST request
    post_data = {'goal': 'Learn Python', 'deadline': '2024-12-31'}
    post_response = api_client.post("/api/goals", json=post_data)
    if post_response:
        print("POST response:", post_response.json())

    # Example PUT request
    put_data = {'goal': 'Master Python', 'deadline': '2025-12-31'}
    put_response = api_client.put("/api/goals/1", json=put_data)
    if put_response:
        print("PUT response:", put_response.json())

    # Example DELETE request
    delete_response = api_client.delete("/api/goals/1")
    if delete_response:
        print("DELETE response:", delete_response.status_code)
