from forta_agent import FindingSeverity, FindingType, create_transaction_event
from agent import handle_transaction
from src.constants import MULTI_SIG_MAINNET_ADDRESS, ADDRESS_LIST

class TestMultiSigInteraction:
    def test_returns_empty_findings_if_no_address(self):
        tx_event = create_transaction_event({
            'transaction': {
                'from': "0x",
                'to': MULTI_SIG_MAINNET_ADDRESS,
            }})
        findings = handle_transaction(tx_event)
        assert len(findings) == 0

    def test_returns_finding_if_found(self):
        tx_event = create_transaction_event({
            'transaction': {
                'from': ADDRESS_LIST[0],
                'to': MULTI_SIG_MAINNET_ADDRESS
            }
        })
        findings = handle_transaction(tx_event)
        assert len(findings) != 0

    def test_returns_empty_if_not_multisig(self):
        tx_event = create_transaction_event({
            'transaction': {
                'from': ADDRESS_LIST[0],
                'to': "0x"
            }
        })
        findings = handle_transaction(tx_event)
        assert len(findings) == 0

    