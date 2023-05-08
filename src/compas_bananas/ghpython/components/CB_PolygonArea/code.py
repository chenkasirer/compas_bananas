from compas_bananas.algorithms import polygon_area
from ghpythonlib.componentbase import executingcomponent as component


class CBPolygonArea(component):
    def RunScript(self, polygon):
        return polygon_area(polygon)
