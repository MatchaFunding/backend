import type { Sequelize } from "sequelize";
import { auth_group as _auth_group } from "./auth_group";
import type { auth_groupAttributes, auth_groupCreationAttributes } from "./auth_group";
import { auth_group_permissions as _auth_group_permissions } from "./auth_group_permissions";
import type { auth_group_permissionsAttributes, auth_group_permissionsCreationAttributes } from "./auth_group_permissions";
import { auth_permission as _auth_permission } from "./auth_permission";
import type { auth_permissionAttributes, auth_permissionCreationAttributes } from "./auth_permission";
import { auth_user as _auth_user } from "./auth_user";
import type { auth_userAttributes, auth_userCreationAttributes } from "./auth_user";
import { auth_user_groups as _auth_user_groups } from "./auth_user_groups";
import type { auth_user_groupsAttributes, auth_user_groupsCreationAttributes } from "./auth_user_groups";
import { auth_user_user_permissions as _auth_user_user_permissions } from "./auth_user_user_permissions";
import type { auth_user_user_permissionsAttributes, auth_user_user_permissionsCreationAttributes } from "./auth_user_user_permissions";
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
import { django_admin_log as _django_admin_log } from "./django_admin_log";
import type { django_admin_logAttributes, django_admin_logCreationAttributes } from "./django_admin_log";
import { django_content_type as _django_content_type } from "./django_content_type";
import type { django_content_typeAttributes, django_content_typeCreationAttributes } from "./django_content_type";
import { django_migrations as _django_migrations } from "./django_migrations";
import type { django_migrationsAttributes, django_migrationsCreationAttributes } from "./django_migrations";
import { django_session as _django_session } from "./django_session";
import type { django_sessionAttributes, django_sessionCreationAttributes } from "./django_session";

export {
  _auth_group as auth_group,
  _auth_group_permissions as auth_group_permissions,
  _auth_permission as auth_permission,
  _auth_user as auth_user,
  _auth_user_groups as auth_user_groups,
  _auth_user_user_permissions as auth_user_user_permissions,
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
  _django_admin_log as django_admin_log,
  _django_content_type as django_content_type,
  _django_migrations as django_migrations,
  _django_session as django_session,
};

export type {
  auth_groupAttributes,
  auth_groupCreationAttributes,
  auth_group_permissionsAttributes,
  auth_group_permissionsCreationAttributes,
  auth_permissionAttributes,
  auth_permissionCreationAttributes,
  auth_userAttributes,
  auth_userCreationAttributes,
  auth_user_groupsAttributes,
  auth_user_groupsCreationAttributes,
  auth_user_user_permissionsAttributes,
  auth_user_user_permissionsCreationAttributes,
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
  django_admin_logAttributes,
  django_admin_logCreationAttributes,
  django_content_typeAttributes,
  django_content_typeCreationAttributes,
  django_migrationsAttributes,
  django_migrationsCreationAttributes,
  django_sessionAttributes,
  django_sessionCreationAttributes,
};

export function initModels(sequelize: Sequelize) {
  const auth_group = _auth_group.initModel(sequelize);
  const auth_group_permissions = _auth_group_permissions.initModel(sequelize);
  const auth_permission = _auth_permission.initModel(sequelize);
  const auth_user = _auth_user.initModel(sequelize);
  const auth_user_groups = _auth_user_groups.initModel(sequelize);
  const auth_user_user_permissions = _auth_user_user_permissions.initModel(sequelize);
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
  const django_admin_log = _django_admin_log.initModel(sequelize);
  const django_content_type = _django_content_type.initModel(sequelize);
  const django_migrations = _django_migrations.initModel(sequelize);
  const django_session = _django_session.initModel(sequelize);

  auth_group_permissions.belongsTo(auth_group, { as: "group", foreignKey: "group_id"});
  auth_group.hasMany(auth_group_permissions, { as: "auth_group_permissions", foreignKey: "group_id"});
  auth_user_groups.belongsTo(auth_group, { as: "group", foreignKey: "group_id"});
  auth_group.hasMany(auth_user_groups, { as: "auth_user_groups", foreignKey: "group_id"});
  auth_group_permissions.belongsTo(auth_permission, { as: "permission", foreignKey: "permission_id"});
  auth_permission.hasMany(auth_group_permissions, { as: "auth_group_permissions", foreignKey: "permission_id"});
  auth_user_user_permissions.belongsTo(auth_permission, { as: "permission", foreignKey: "permission_id"});
  auth_permission.hasMany(auth_user_user_permissions, { as: "auth_user_user_permissions", foreignKey: "permission_id"});
  auth_user_groups.belongsTo(auth_user, { as: "user", foreignKey: "user_id"});
  auth_user.hasMany(auth_user_groups, { as: "auth_user_groups", foreignKey: "user_id"});
  auth_user_user_permissions.belongsTo(auth_user, { as: "user", foreignKey: "user_id"});
  auth_user.hasMany(auth_user_user_permissions, { as: "auth_user_user_permissions", foreignKey: "user_id"});
  django_admin_log.belongsTo(auth_user, { as: "user", foreignKey: "user_id"});
  auth_user.hasMany(django_admin_log, { as: "django_admin_logs", foreignKey: "user_id"});
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
  auth_permission.belongsTo(django_content_type, { as: "content_type", foreignKey: "content_type_id"});
  django_content_type.hasMany(auth_permission, { as: "auth_permissions", foreignKey: "content_type_id"});
  django_admin_log.belongsTo(django_content_type, { as: "content_type", foreignKey: "content_type_id"});
  django_content_type.hasMany(django_admin_log, { as: "django_admin_logs", foreignKey: "content_type_id"});

  return {
    auth_group: auth_group,
    auth_group_permissions: auth_group_permissions,
    auth_permission: auth_permission,
    auth_user: auth_user,
    auth_user_groups: auth_user_groups,
    auth_user_user_permissions: auth_user_user_permissions,
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
    django_admin_log: django_admin_log,
    django_content_type: django_content_type,
    django_migrations: django_migrations,
    django_session: django_session,
  };
}
