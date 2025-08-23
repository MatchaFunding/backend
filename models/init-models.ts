import type { Sequelize } from "sequelize";
import { backend_beneficiario as _backend_beneficiario } from "./backend_beneficiario";
import type { backend_beneficiarioAttributes, backend_beneficiarioCreationAttributes } from "./backend_beneficiario";
import { backend_colaborador as _backend_colaborador } from "./backend_colaborador";
import type { backend_colaboradorAttributes, backend_colaboradorCreationAttributes } from "./backend_colaborador";
import { backend_consorcio as _backend_consorcio } from "./backend_consorcio";
import type { backend_consorcioAttributes, backend_consorcioCreationAttributes } from "./backend_consorcio";
import { backend_financiador as _backend_financiador } from "./backend_financiador";
import type { backend_financiadorAttributes, backend_financiadorCreationAttributes } from "./backend_financiador";
import { backend_instrumento as _backend_instrumento } from "./backend_instrumento";
import type { backend_instrumentoAttributes, backend_instrumentoCreationAttributes } from "./backend_instrumento";
import { backend_miembro as _backend_miembro } from "./backend_miembro";
import type { backend_miembroAttributes, backend_miembroCreationAttributes } from "./backend_miembro";
import { backend_persona as _backend_persona } from "./backend_persona";
import type { backend_personaAttributes, backend_personaCreationAttributes } from "./backend_persona";
import { backend_postulacion as _backend_postulacion } from "./backend_postulacion";
import type { backend_postulacionAttributes, backend_postulacionCreationAttributes } from "./backend_postulacion";
import { backend_proyecto as _backend_proyecto } from "./backend_proyecto";
import type { backend_proyectoAttributes, backend_proyectoCreationAttributes } from "./backend_proyecto";
import { backend_usuario as _backend_usuario } from "./backend_usuario";
import type { backend_usuarioAttributes, backend_usuarioCreationAttributes } from "./backend_usuario";
import { django_migrations as _django_migrations } from "./django_migrations";
import type { django_migrationsAttributes, django_migrationsCreationAttributes } from "./django_migrations";

export {
  _backend_beneficiario as backend_beneficiario,
  _backend_colaborador as backend_colaborador,
  _backend_consorcio as backend_consorcio,
  _backend_financiador as backend_financiador,
  _backend_instrumento as backend_instrumento,
  _backend_miembro as backend_miembro,
  _backend_persona as backend_persona,
  _backend_postulacion as backend_postulacion,
  _backend_proyecto as backend_proyecto,
  _backend_usuario as backend_usuario,
  _django_migrations as django_migrations,
};

export type {
  backend_beneficiarioAttributes,
  backend_beneficiarioCreationAttributes,
  backend_colaboradorAttributes,
  backend_colaboradorCreationAttributes,
  backend_consorcioAttributes,
  backend_consorcioCreationAttributes,
  backend_financiadorAttributes,
  backend_financiadorCreationAttributes,
  backend_instrumentoAttributes,
  backend_instrumentoCreationAttributes,
  backend_miembroAttributes,
  backend_miembroCreationAttributes,
  backend_personaAttributes,
  backend_personaCreationAttributes,
  backend_postulacionAttributes,
  backend_postulacionCreationAttributes,
  backend_proyectoAttributes,
  backend_proyectoCreationAttributes,
  backend_usuarioAttributes,
  backend_usuarioCreationAttributes,
  django_migrationsAttributes,
  django_migrationsCreationAttributes,
};

export function initModels(sequelize: Sequelize) {
  const backend_beneficiario = _backend_beneficiario.initModel(sequelize);
  const backend_colaborador = _backend_colaborador.initModel(sequelize);
  const backend_consorcio = _backend_consorcio.initModel(sequelize);
  const backend_financiador = _backend_financiador.initModel(sequelize);
  const backend_instrumento = _backend_instrumento.initModel(sequelize);
  const backend_miembro = _backend_miembro.initModel(sequelize);
  const backend_persona = _backend_persona.initModel(sequelize);
  const backend_postulacion = _backend_postulacion.initModel(sequelize);
  const backend_proyecto = _backend_proyecto.initModel(sequelize);
  const backend_usuario = _backend_usuario.initModel(sequelize);
  const django_migrations = _django_migrations.initModel(sequelize);

  backend_consorcio.belongsTo(backend_beneficiario, { as: "PrimerBeneficiario", foreignKey: "PrimerBeneficiario_id"});
  backend_beneficiario.hasMany(backend_consorcio, { as: "backend_consorcios", foreignKey: "PrimerBeneficiario_id"});
  backend_consorcio.belongsTo(backend_beneficiario, { as: "SegundoBeneficiario", foreignKey: "SegundoBeneficiario_id"});
  backend_beneficiario.hasMany(backend_consorcio, { as: "SegundoBeneficiario_backend_consorcios", foreignKey: "SegundoBeneficiario_id"});
  backend_miembro.belongsTo(backend_beneficiario, { as: "Beneficiario", foreignKey: "Beneficiario_id"});
  backend_beneficiario.hasMany(backend_miembro, { as: "backend_miembros", foreignKey: "Beneficiario_id"});
  backend_postulacion.belongsTo(backend_beneficiario, { as: "Beneficiario", foreignKey: "Beneficiario_id"});
  backend_beneficiario.hasMany(backend_postulacion, { as: "backend_postulacions", foreignKey: "Beneficiario_id"});
  backend_proyecto.belongsTo(backend_beneficiario, { as: "Beneficiario", foreignKey: "Beneficiario_id"});
  backend_beneficiario.hasMany(backend_proyecto, { as: "backend_proyectos", foreignKey: "Beneficiario_id"});
  backend_instrumento.belongsTo(backend_financiador, { as: "Financiador", foreignKey: "Financiador_id"});
  backend_financiador.hasMany(backend_instrumento, { as: "backend_instrumentos", foreignKey: "Financiador_id"});
  backend_postulacion.belongsTo(backend_instrumento, { as: "Instrumento", foreignKey: "Instrumento_id"});
  backend_instrumento.hasMany(backend_postulacion, { as: "backend_postulacions", foreignKey: "Instrumento_id"});
  backend_colaborador.belongsTo(backend_persona, { as: "Persona", foreignKey: "Persona_id"});
  backend_persona.hasMany(backend_colaborador, { as: "backend_colaboradors", foreignKey: "Persona_id"});
  backend_miembro.belongsTo(backend_persona, { as: "Persona", foreignKey: "Persona_id"});
  backend_persona.hasMany(backend_miembro, { as: "backend_miembros", foreignKey: "Persona_id"});
  backend_usuario.belongsTo(backend_persona, { as: "Persona", foreignKey: "Persona_id"});
  backend_persona.hasMany(backend_usuario, { as: "backend_usuarios", foreignKey: "Persona_id"});
  backend_colaborador.belongsTo(backend_proyecto, { as: "Proyecto", foreignKey: "Proyecto_id"});
  backend_proyecto.hasMany(backend_colaborador, { as: "backend_colaboradors", foreignKey: "Proyecto_id"});
  backend_postulacion.belongsTo(backend_proyecto, { as: "Proyecto", foreignKey: "Proyecto_id"});
  backend_proyecto.hasMany(backend_postulacion, { as: "backend_postulacions", foreignKey: "Proyecto_id"});

  return {
    backend_beneficiario: backend_beneficiario,
    backend_colaborador: backend_colaborador,
    backend_consorcio: backend_consorcio,
    backend_financiador: backend_financiador,
    backend_instrumento: backend_instrumento,
    backend_miembro: backend_miembro,
    backend_persona: backend_persona,
    backend_postulacion: backend_postulacion,
    backend_proyecto: backend_proyecto,
    backend_usuario: backend_usuario,
    django_migrations: django_migrations,
  };
}
