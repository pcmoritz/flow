class BaseRouter:
    def __init__(self, veh_id, router_params):
        """Base class for routing controllers.

        These controllers are used to dynamical change the routes of vehicles
        after initialization.

        Attributes
        ----------
        veh_id: string
            ID of the vehicle this controller is used for
        router_params: dict
            Dictionary of router params
        """
        self.veh_id = veh_id
        self.router_params = router_params

    def choose_route(self, env):
        """The routing method implemented by the controller.

        Parameters
        ----------
        env: Environment type
            see flow/envs/base_env.py

        Returns
        -------
        route: list or None
            The sequence of edges the vehicle should adopt. If a None value
            is returned, the vehicle performs no routing action in the current
            time step.
        """
        raise NotImplementedError
