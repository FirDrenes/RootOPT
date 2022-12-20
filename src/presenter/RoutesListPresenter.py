import json

from src.presenter.presenter import Presenter


class RoutesListPresenter(Presenter):
    @staticmethod
    def convert_repr_to_obj(present):
        raise NotImplementedError

    @staticmethod
    def convert_obj_to_repr(route_list):
        present = list(map(lambda node: RoutesListPresenter.convert_list_node_to_repr(node), route_list))
        return json.dumps(present)

    @staticmethod
    def convert_list_node_to_repr(node):
        return {
            "route_id": str(node["_id"]),
            "name": node["route_name"]
        }