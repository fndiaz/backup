routers = dict(

    # base router
    BASE=dict(
        default_application='projeto',
	applications=['projeto', 'admin',]
    ),

    projeto=dict(
        default_controller='initial',
        default_function='principal',
	controllers=['initial', 'manager'],
        functions=['home', 'contact', 'about', 'user', 'download', 'account', 
			'gera_pdf', 'gera_zip', 'remover', 'log_eventos',
			'edit', 'interface', 'principal', 'detalhes_clean', 'detalhes_nav', 
			'redireciona', 'addition', 'addition2', 'log_out', 'log_in', 'ligacao', 'permissao', 'principal.pdf']
    )

)
