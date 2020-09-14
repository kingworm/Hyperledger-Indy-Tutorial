import argparse

from indy_common.config_helper import ConfigHelper
from indy_common.config_util import getConfig
from indy_common.txn_util import getTxnOrderedFields

from plenum.common.config_helper import PConfigHelper


class DomainLedger:

    @staticmethod
    def _bootstrap_args_type_dids(dids_str_arg):
        did = []
        i =1 
        for arg in dids_str_arg.split(','):
            arg = str(arg)
            arg = arg.strip()
            if len(arg) != 22:
                raise argparse.ArgumentTypeError("The lenght of did {} should be 22 digit long".format(i))           
            did.append(arg)
            i += 1

        return did

    
    @staticmethod
    def _bootstrap_args_type_verkeys(verkeys_str_arg):
        verkeys = []
        i =1 
        for arg in verkeys_str_arg.split(','):
            arg = str(arg)
            arg = arg.strip()
            if len(arg) != 23:
                raise argparse.ArgumentTypeError("The lenght verification key {} should be 23 digit long".format(i))           
            verkeys.append(arg)
            i += 1

        return verkeys


    @classmethod
    def bootstrap_domain_ledger(cls, config=getConfig(), config_helper_class=PConfigHelper,
                                domainTxnFieldOrder=getTxnOrderedFields(), chroot: str=None):
        parser = argparse.ArgumentParser(description="Generate domain transactions")
        parser.add_argument('--trusteeDids', required=True,
                            help='Trustee Dids, provide comma separated dids',
                            type=cls._bootstrap_args_type_dids)
        parser.add_argument('--trusteeVerkeys', required=True,
                            help='Trustees Verkey, provide comma separated verification keys',
                            type=cls. _bootstrap_args_type_verkeys)
        parser.add_argument('--stewardDids', required=True,
                            help='Stewards Dids, provide comma separated dids',
                            type=cls._bootstrap_args_type_dids)
        parser.add_argument('--stewardVerkeys', required=True,
                            help='Stewards Verkey, provide comma separated verification keys',
                            type=cls. _bootstrap_args_type_verkeys)
        parser.add_argument('--network', required=False,
                            help='Network name (default sandbox)',
                            type=str,               
                            default="sandbox")
        parser.add_argument(
            '--appendToLedgers',
            help="Determine if ledger files needs to be erased "
                 "before writing new information or not",
            action='store_true')  

        args = parser.parse_args()