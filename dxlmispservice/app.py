from __future__ import absolute_import
import logging

from dxlbootstrap.app import Application
from .eventhandlers import *


# Configure local logger
logger = logging.getLogger(__name__)


class MispService(Application):
    """
    The "MISP DXL service library" application class.
    """

    def __init__(self, config_dir):
        """
        Constructor parameters:

        :param config_dir: The location of the configuration files for the
            application
        """
        super(MispService, self).__init__(config_dir, "dxlmispservice.config")

    @property
    def client(self):
        """
        The DXL client used by the application to communicate with the DXL
        fabric
        """
        return self._dxl_client

    @property
    def config(self):
        """
        The application configuration (as read from the "dxlmispservice.config" file)
        """
        return self._config

    def on_run(self):
        """
        Invoked when the application has started running.
        """
        logger.info("On 'run' callback.")

    def on_load_configuration(self, config):
        """
        Invoked after the application-specific configuration has been loaded

        This callback provides the opportunity for the application to parse
        additional configuration properties.

        :param config: The application configuration
        """
        logger.info("On 'load configuration' callback.")

    def on_dxl_connect(self):
        """
        Invoked after the client associated with the application has connected
        to the DXL fabric.
        """
        logger.info("On 'DXL connect' callback.")
    
    def on_register_event_handlers(self):
        """
        Invoked when event handlers should be registered with the application
        """
        # Register event callback 'misp_event'
        logger.info("Registering event callback: %s", "misp_event")
        self.add_event_callback("/opendxl-misp/service/notifications", MispEventCallback(self), True)
