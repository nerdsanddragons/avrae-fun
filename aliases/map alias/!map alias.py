!alias map {{args = &ARGS &}}
{{defaults = '{"size":"26x14", "background":"https://t.ly/KgwG", "options":"hd"}'}}
{{get_gvar("5eb8d24b-d660-42e5-bbea-47a659bb0827").replace('"@@@"', str(args)).replace('"&&&"', defaults)}}




!alias move {{args = &ARGS &}}
{{args = ['-t', name, '-move']+args if args else []}}
{{defaults = '{"size":"26x14", "background":"https://t.ly/KgwG", "options":"hd"}'}}
{{get_gvar("5eb8d24b-d660-42e5-bbea-47a659bb0827").replace('"@@@"', str(args)).replace('"&&&"', defaults)}}




!alias over {{args=&ARGS&}}
{{g=load_json(get_gvar("d456fdfa-a292-42a1-ab00-b884e79b702f"))}}
{{_=[g.update(load_json(get_gvar(spells))) for spells in load_json(get('mapOverlays','{}')) if get_gvar(spells)]}}
{{args=[g[x] if x in g else ([g[y] for y in g if x.lower() in y.lower()]+[x])[0] for x in args]}}
{{args=['-t',name,'-over']+args if args else []}}{{defaults='{"size":"", "background":"", "options":""}' }}
{{get_gvar("5eb8d24b-d660-42e5-bbea-47a659bb0827").replace('"@@@"',str(args)).replace('"&&&"', defaults)}}