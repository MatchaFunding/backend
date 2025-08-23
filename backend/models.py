from django.db import models

'''
Clase que representa la empresa, emprendimiento, grupo de investigacion, etc.
que desea postular al fondo. La informacion debe regirse por la descripcion
legal de la empresa.
https://www.registrodeempresasysociedades.cl/MarcaDominio.aspx
https://www.rutificador.co/empresas/buscar
https://www.boletaofactura.com/
https://registros19862.gob.cl/
https://dequienes.cl/
'''
class Beneficiario(models.Model):
	REGIONES = {
		"AP": "Arica y Parinacota",
		"TA": "Tarapacá",
		"AN": "Antofagasta",
		"AT": "Atacama",
		"CO": "Coquimbo",
		"VA": "Valparaíso",
		"RM": "de Santiago",
		"LI": "Libertador General Bernardo O'Higgins",
		"ML": "Maule",
		"NB": "Ñuble",
		"BI": "Biobío",
		"AR": "La Araucanía",
		"LR": "Los Ríos",
		"LL": "Los Lagos",
		"AI": "Aysén del General Carlos Ibáñez del Campo",
		"MA": "Magallanes y de la Antártica Chilena"
	}
	# https://www.sii.cl/mipyme/emprendedor/documentos/fac_Datos_Comenzar_2.htm
	PERSONA = {
		"JU": "Juridica",
		"NA": "Natural"
	}
	# https://ipp.cl/general/tipos-de-empresas-en-chile/
	EMPRESA = {
		"SA": "Sociedad Anonima",
		"SRL": "Sociedad de Responsabilidad Limitada",
		"SPA": "Sociedad por Acciones",
		"EIRL": "Empresa Individual de Responsabilidad Limitada"
	}
	# https://corfo.cl/sites/cpp/programasyconvocatorias/
	PERFIL = {
		"EMP": "Empresa",
		"EXT": "Extranjero",
		"INS": "Institucion",
		"MED": "Intermediario",
		"ORG": "Organizacion",
		"PER": "Persona"
	}
	ID = models.BigAutoField(primary_key=True)
	Nombre = models.CharField(max_length=100)
	FechaDeCreacion = models.DateField()
	RegionDeCreacion = models.CharField(max_length=30, choices=REGIONES)
	Direccion = models.CharField(max_length=300)
	TipoDePersona = models.CharField(max_length=30, choices=PERSONA)
	TipoDeEmpresa = models.CharField(max_length=30, choices=EMPRESA)
	Perfil = models.CharField(max_length=30, choices=PERFIL)
	RUTdeEmpresa = models.CharField(max_length=12)
	RUTdeRepresentante = models.CharField(max_length=12)

'''
Clase que representa los proyectos de una misma empresa.
https://www.boletaofactura.com/
'''
class Proyecto(models.Model):
	REGIONES = {
		"AP": "Arica y Parinacota",
		"TA": "Tarapacá",
		"AN": "Antofagasta",
		"AT": "Atacama",
		"CO": "Coquimbo",
		"VA": "Valparaíso",
		"RM": "de Santiago",
		"LI": "Libertador General Bernardo O'Higgins",
		"ML": "Maule",
		"NB": "Ñuble",
		"BI": "Biobío",
		"AR": "La Araucanía",
		"LR": "Los Ríos",
		"LL": "Los Lagos",
		"AI": "Aysén del General Carlos Ibáñez del Campo",
		"MA": "Magallanes y de la Antártica Chilena"
	}
	ID = models.BigAutoField(primary_key=True)
	Beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
	Titulo = models.CharField(max_length=300)
	Descripcion = models.CharField(max_length=500)
	DuracionEnMesesMinimo = models.IntegerField()
	DuracionEnMesesMaximo = models.IntegerField()
	Alcance = models.CharField(max_length=30, choices=REGIONES)
	Area = models.CharField(max_length=100)

'''
Clase que representa a una persona natural, la cual puede ser miembro de una empresa o proyecto.
Abajo de este estan las asociaciones entre persona y agrupacion.
https://www.nombrerutyfirma.com/nombre
https://www.nombrerutyfirma.com/rut
https://www.volanteomaleta.com/
'''
class Persona(models.Model):
	SEXO = {
		"VAR": "Hombre",
		"MUJ": "Mujer",
		"NA": "Otro"
	}
	ID = models.BigAutoField(primary_key=True)
	Nombre = models.CharField(max_length=200)
	Sexo = models.CharField(max_length=30, choices=SEXO)
	RUT = models.CharField(max_length=12)

'''
Clase que representa a una persona que es parte de una empresa, agrupacion o grupo de investigacion.
https://dequienes.cl/
'''
class Miembro(models.Model):
	ID = models.BigAutoField(primary_key=True)
	Persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
	Beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)

'''
Clase que representa a una persona que es parte de un proyecto que busca fondos.
https://dequienes.cl/
'''
class Colaborador(models.Model):
	ID = models.BigAutoField(primary_key=True)
	Persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
	Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

'''
Clase que representa a un usuario de matchafunding.
'''
class Usuario(models.Model):
	ID = models.BigAutoField(primary_key=True)
	Persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
	NombreDeUsuario = models.CharField(max_length=200, null=False)
	Contrasena = models.CharField(max_length=200, null=False)
	Correo = models.EmailField(max_length=200, null=False)

'''
Agrupacion de multiples empresas y agrupaciones que pretenden postular
en conjunto a un instrumento / fondo comun.
'''
class Consorcio(models.Model):
	ID = models.BigAutoField(primary_key=True)
	PrimerBeneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE, related_name='primero')
	SegundoBeneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE, related_name='segundo')

'''
Clase que representa las entes financieras que ofrecen los fondos.
En muchos sentidos operan de la misma forma que las entes benficiarias,
lo unico que cambia en rigor son sus relaciones con las otras clases.
https://www.registrodeempresasysociedades.cl/MarcaDominio.aspx
https://www.rutificador.co/empresas/buscar
https://registros19862.gob.cl/
https://dequienes.cl/
'''
class Financiador(models.Model):
	REGIONES = {
		"AP": "Arica y Parinacota",
		"TA": "Tarapacá",
		"AN": "Antofagasta",
		"AT": "Atacama",
		"CO": "Coquimbo",
		"VA": "Valparaíso",
		"RM": "de Santiago",
		"LI": "Libertador General Bernardo O'Higgins",
		"ML": "Maule",
		"NB": "Ñuble",
		"BI": "Biobío",
		"AR": "La Araucanía",
		"LR": "Los Ríos",
		"LL": "Los Lagos",
		"AI": "Aysén del General Carlos Ibáñez del Campo",
		"MA": "Magallanes y de la Antártica Chilena"
	}
	# https://www.sii.cl/mipyme/emprendedor/documentos/fac_Datos_Comenzar_2.htm
	PERSONA = {
		"JU": "Juridica",
		"NA": "Natural"
	}
	# https://ipp.cl/general/tipos-de-empresas-en-chile/
	EMPRESA = {
		"SA": "Sociedad Anonima",
		"SRL": "Sociedad de Responsabilidad Limitada",
		"SPA": "Sociedad por Acciones",
		"EIRL": "Empresa Individual de Responsabilidad Limitada"
	}
	# https://corfo.cl/sites/cpp/programasyconvocatorias/
	PERFIL = {
		"EMP": "Empresa",
		"EXT": "Extranjero",
		"INS": "Institucion",
		"MED": "Intermediario",
		"ORG": "Organizacion",
		"PER": "Persona"
	}
	ID = models.BigAutoField(primary_key=True)
	Nombre = models.CharField(max_length=100)
	FechaDeCreacion = models.DateField()
	RegionDeCreacion = models.CharField(max_length=30, choices=REGIONES)
	Direccion = models.CharField(max_length=300)
	TipoDePersona = models.CharField(max_length=30, choices=PERSONA)
	TipoDeEmpresa = models.CharField(max_length=30, choices=EMPRESA)
	Perfil = models.CharField(max_length=30, choices=PERFIL)
	RUTdeEmpresa = models.CharField(max_length=12)
	RUTdeRepresentante = models.CharField(max_length=12)

'''
Clase que representa los fondos concursables a los que los proyectos pueden postular.
Esta clase contiene todos los parametros y requisitos que dictan la posterior evaluacion.
Representa tanto los fondos actuales como los historicos, en donde la fecha de cierre
indica a cual de los dos corresponde.
Recursos de fondos historicos:
http://wapp.corfo.cl/transparencia/home/Subsidios.aspx
https://github.com/ANID-GITHUB?tab=repositories
https://datainnovacion.cl/api
'''
class Instrumento(models.Model):
	REGIONES = {
		"AP": "Arica y Parinacota",
		"TA": "Tarapacá",
		"AN": "Antofagasta",
		"AT": "Atacama",
		"CO": "Coquimbo",
		"VA": "Valparaíso",
		"RM": "de Santiago",
		"LI": "Libertador General Bernardo O'Higgins",
		"ML": "Maule",
		"NB": "Ñuble",
		"BI": "Biobío",
		"AR": "La Araucanía",
		"LR": "Los Ríos",
		"LL": "Los Lagos",
		"AI": "Aysén del General Carlos Ibáñez del Campo",
		"MA": "Magallanes y de la Antártica Chilena"
	}
	# https://corfo.cl/sites/cpp/programasyconvocatorias/
	ESTADO = {
		"PRX": "Próximo",
		"ABI": "Abierto",
		"EVA": "En evaluación",
		"ADJ": "Adjudicado",
		"SUS": "Suspendido",
		"PAY": "Patrocinio Institucional",
		"DES": "Desierto",
		"CER": "Cerrrado"
	}
	# https://corfo.cl/sites/cpp/programasyconvocatorias/
	BENEFICIO = {
		"CAP": "Capacitacion",
		"RIE": "Capital de riesgo",
		"CRE": "Creditos",
		"GAR": "Garantias",
		"MUJ": "Incentivo mujeres",
		"OTR": "Otros incentivos",
		"SUB": "Subsidios"
	}
	# https://corfo.cl/sites/cpp/programasyconvocatorias/
	PERSONA = {
		"EMP": "Empresa",
		"EXT": "Extranjero",
		"INS": "Institucion",
		"MED": "Intermediario",
		"ORG": "Organizacion",
		"PER": "Persona"
	}
	ID = models.BigAutoField(primary_key=True)
	Titulo = models.CharField(max_length=200)
	Financiador = models.ForeignKey(Financiador, on_delete=models.CASCADE)
	Alcance = models.CharField(max_length=30, choices=REGIONES)
	Descripcion = models.CharField(max_length=1000)
	FechaDeApertura = models.DateField()
	FechaDeCierre = models.DateField()
	DuracionEnMeses = models.IntegerField()
	Beneficios = models.CharField(max_length=1000)
	Requisitos = models.CharField(max_length=1000)
	MontoMinimo = models.IntegerField()
	MontoMaximo = models.IntegerField()
	Estado = models.CharField(max_length=30, choices=ESTADO)
	TipoDeBeneficio = models.CharField(max_length=30, choices=BENEFICIO)
	TipoDePerfil = models.CharField(max_length=30, choices=PERSONA)
	EnlaceDelDetalle = models.URLField(max_length=300)
	EnlaceDeLaFoto = models.URLField(max_length=300)

'''
Clase que representa las postulaciones de un proyecto a un fondo
https://registros19862.gob.cl/
'''
class Postulacion(models.Model):
	RESULTADO = {
		"ADJ": "Adjudicado",
		"REC": "Rechazado",
		"PEN": "Pendiente"
	}
	ID = models.BigAutoField(primary_key=True)
	Beneficiario = models.ForeignKey(Beneficiario, null=False, on_delete=models.CASCADE)
	Proyecto = models.ForeignKey(Proyecto, null=False, on_delete=models.CASCADE)
	Instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)
	Resultado = models.CharField(max_length=30, choices=RESULTADO)
	MontoObtenido = models.IntegerField()
	FechaDePostulacion = models.DateField()
	FechaDeResultado = models.DateField()
	Detalle = models.CharField(max_length=1000)