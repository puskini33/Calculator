class WorldState(object):

    def __init__(self):
        self.variables = {}

    def clone(self):
        temporary_world_state = WorldState()
        temporary_world_state.variables = self.variables
        return temporary_world_state
