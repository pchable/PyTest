class Edge:
    """Connector"""

    def __init__(self, p_start, p_end):
        self._start = p_start
        self._end = p_end

    def connect(self, p_other: object):
        connected = Edge("", "")
        connected._start = self._start
        connected._end = p_other._end
        return connected

    def print(self):
        print("\nEdge:")
        print("\tStart: " + self._start)
        print("\tEnd: " + self._end)