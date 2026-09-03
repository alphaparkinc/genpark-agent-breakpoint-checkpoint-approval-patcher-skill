from client import AgentBreakpointCheckpointApprovalPatcherClient

def main():
    client = AgentBreakpointCheckpointApprovalPatcherClient()
    res = client.pause_at_breakpoint_and_patch('chk_01', 'SEND_EMAIL', 0, 'APPROVED')
    print('Breakpoint Checkpoint Patcher: ' + res['breakpoint_event_id'] + ' (Checkpoint: ' + res['checkpoint_id'] + ')')
    print('Applied: ' + str(res['state_mutation_applied']) + ' | Status: ' + res['resumed_graph_execution_status'])
    print('Audit URL: ' + res['audit_trail_signature_url'])

if __name__ == '__main__':
    main()
