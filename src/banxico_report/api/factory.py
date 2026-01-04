import os
from .provider import SIEProvider

class SIEProviderFactory:
    """
    Factory for instantiating the appropriate SIEProvider based on environment.
    """
    
    @staticmethod
    def get_provider(token: str = None) -> SIEProvider:
        """
        Returns a SIEProvider instance.
        
        If INFLACIONAL_ENV is 'test', returns a MockSIEProvider.
        Otherwise, returns a RealSIEProvider (defaulting to production).
        """
        env = os.getenv("INFLACIONAL_ENV", "production").lower()
        
        if env == "test":
            from tests.mocks.provider import MockSIEProvider
            # We don't need a token for mock provider, 
            # but we pass it anyway to keep signature consistency if needed
            return MockSIEProvider()
        else:
            from .real import RealSIEProvider
            return RealSIEProvider(token=token)
