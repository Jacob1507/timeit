from tests.utils import resolve_url

from .utils import MOCK_DT, TestClientMixin


class TestTaskApi(TestClientMixin):
    payload = dict(title="Hello world", completed=False, time=MOCK_DT)

    def _create_task(self):
        url = resolve_url("task_create")
        response = self.client.post(url, json=self.payload)
        assert response.status_code == self.STATUS_OK
        return response

    def test_list_empty(self):
        url = resolve_url("task_list")
        response = self.client.get(url)
        assert response.status_code == self.STATUS_OK
        assert response.json() == [], response.json()

    def test_create_task(self):
        response = self._create_task()
        # get list
        url = resolve_url("task_list")
        response = self.client.get(url)
        assert len(response.json()) == 1

    def test_update_task(self):
        response = self._create_task()
        response_data = response.json()
        assert response_data["completed"] is False
        # update
        url = resolve_url("task_update", task_id=response_data["id"])
        self.payload["completed"] = True
        response = self.client.put(url, json=self.payload)
        # get detail
        url = resolve_url("task_detail", task_id=response_data["id"])
        response = self.client.get(url)
        response_data = response.json()
        assert response_data["completed"] is True

    def test_delete_task(self):
        response = self._create_task()
        response_data = response.json()
        # delete
        url = resolve_url("task_delete", task_id=response_data["id"])
        response = self.client.delete(url)
        assert response.status_code == self.STATUS_OK
        # get detail
        url = resolve_url("task_detail", task_id=response_data["id"])
        response = self.client.get(url)
        assert response.json() is None
