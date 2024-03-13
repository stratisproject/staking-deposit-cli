from typing import Dict, NamedTuple
from eth_utils import decode_hex

DEPOSIT_CLI_VERSION = '2.7.0'


class BaseChainSetting(NamedTuple):
    NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes
    GENESIS_VALIDATORS_ROOT: bytes


MAINNET = 'mainnet'
AURORIA = 'auroria'

# Mainnet setting
MainnetSetting = BaseChainSetting(
    NETWORK_NAME=MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('0a000000'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('a73c6c40923a73d0ba772eb3791352c8f6cf42bd72c4677e9153d5a14de991e5'))
# Auroria setting
AuroriaSettings = BaseChainSetting(
    NETWORK_NAME=AURORIA, GENESIS_FORK_VERSION=bytes.fromhex('0a000a14'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('55e9926fc5accb8addfee35751d43c1313ae12780b6ad29e21ea32da97b33d8f')
)

ALL_CHAINS: Dict[str, BaseChainSetting] = {
    MAINNET: MainnetSetting,
    AURORIA: AuroriaSettings,
}


def get_chain_setting(chain_name: str = MAINNET) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]


def get_devnet_chain_setting(network_name: str,
                             genesis_fork_version: str,
                             genesis_validator_root: str) -> BaseChainSetting:
    return BaseChainSetting(
        NETWORK_NAME=network_name,
        GENESIS_FORK_VERSION=decode_hex(genesis_fork_version),
        GENESIS_VALIDATORS_ROOT=decode_hex(genesis_validator_root),
    )
