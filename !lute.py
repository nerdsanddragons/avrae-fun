!alias lute {{set_cvar_nx("lute",get_gvar("1004770f-0cc0-43ae-8a06-c7d840d2f61a"))}}{{a,spells=&ARGS&,load_json(lute)}}{{match=[spell for spell in spells if not spells[spell].used and a and a[0].lower() in spell.lower()]}}{{match=match[0] if match else ""}}{{f'{("i cast" if combat() and combat().me else "cast")} "{match}" -i {" ".join(a[1:]) if a else ""}'+(f' -l {spells[match].level}' if "level" in spells[match] else "") if match else f'embed -title "Doss Lute, Instrument of the Bards'+(', Regains its Spells!' if "reset" in "".join(a) else '')+f'" -color {color} -thumb {image} {get_gvar("a48e386d-f41c-4730-9f7d-a6a442050b64")}'}}
{{spells.update({f'{match}':load_json(dump_json(spells[match]).replace("false","true"))}) if match else ""}}
{{set_cvar("lute",dump_json(spells) if not ("reset" in "".join(a)) else lute.replace("true","false"))}}
{{spells=load_json(lute)}}
{{UUSD,USD=[spell+(f' ({spells[spell].level}{"nd" if spells[spell].level==2 else "rd" if spells[spell].level==3 else "th"} level)' if "level" in spells[spell] else "") for spell in spells if not spells[spell].used],[spell+(f' ({spells[spell].level}{"nd" if spells[spell].level==2 else "rd" if spells[spell].level==3 else "th"} level)' if "level" in spells[spell] else "") for spell in spells if spells[spell].used]}}
{{(f' -f "Available Spells|{", ".join(UUSD)}"' if len(UUSD) else '')+(f' -f "Used Spells|{", ".join(USD)}"' if len(USD) else '')}}