import json
from pydoc_data.topics import topics
import eth_abi
from eth_utils import event_abi_to_log_topic
from forta_agent import create_transaction_event
from agent import handle_transaction
from src.constants import MULTI_SIG_ABI, MULTI_SIG_MAINNET_ADDRESS


class TestMultiSigEvent:
    
    def test_returns_empty_findings_if_address_is_wrong(self):
        data = eth_abi.encode_abi(["address"], [MULTI_SIG_MAINNET_ADDRESS])
        topics = [event_abi_to_log_topic(json.loads(MULTI_SIG_ABI)), data]
        tx_event = create_transaction_event({
            #
        })
        findings = handle_transaction(tx_event)
        assert len(findings) == 0

TestMultiSigEvent().test_returns_empty_findings_if_address_is_wrong()