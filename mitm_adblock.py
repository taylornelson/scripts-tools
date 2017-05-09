def request(context, flow):
    if 'ads' in flow.request.url:
        context.kill_flow(flow)