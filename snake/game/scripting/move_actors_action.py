from game.scripting.action import Action
import constants


class MoveActorsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def execute(self, cast, script):
        """Executes the move actors action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()
            
        snake_one = cast.get_first_actor("snake_one")
        snake_two = cast.get_first_actor("snake_two")
        snake_one.grow_tail(constants.TAIL_GROWTH)
        snake_two.grow_tail(constants.TAIL_GROWTH)