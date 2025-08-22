import * as Sequelize from 'sequelize';
import { DataTypes, Model, Optional } from 'sequelize';
import type { backend_consorcio, backend_consorcioId } from './backend_consorcio';
import type { backend_miembro, backend_miembroId } from './backend_miembro';
import type { backend_postulacion, backend_postulacionId } from './backend_postulacion';
import type { backend_proyecto, backend_proyectoId } from './backend_proyecto';
import type { backend_ubicacion, backend_ubicacionId } from './backend_ubicacion';

export interface backend_beneficiarioAttributes {
  ID: number;
  Nombre: string;
  FechaDeCreacion: string;
  TipoDePersona: string;
  TipoDeEmpresa: string;
  Perfil: string;
  RUTdeEmpresa: string;
  RUTdeRepresentante: string;
  LugarDeCreacion_id: number;
}

export type backend_beneficiarioPk = "ID";
export type backend_beneficiarioId = backend_beneficiario[backend_beneficiarioPk];
export type backend_beneficiarioOptionalAttributes = "ID";
export type backend_beneficiarioCreationAttributes = Optional<backend_beneficiarioAttributes, backend_beneficiarioOptionalAttributes>;

export class backend_beneficiario extends Model<backend_beneficiarioAttributes, backend_beneficiarioCreationAttributes> implements backend_beneficiarioAttributes {
  ID!: number;
  Nombre!: string;
  FechaDeCreacion!: string;
  TipoDePersona!: string;
  TipoDeEmpresa!: string;
  Perfil!: string;
  RUTdeEmpresa!: string;
  RUTdeRepresentante!: string;
  LugarDeCreacion_id!: number;

  // backend_beneficiario hasMany backend_consorcio via PrimerBeneficiario_id
  backend_consorcios!: backend_consorcio[];
  getBackend_consorcios!: Sequelize.HasManyGetAssociationsMixin<backend_consorcio>;
  setBackend_consorcios!: Sequelize.HasManySetAssociationsMixin<backend_consorcio, backend_consorcioId>;
  addBackend_consorcio!: Sequelize.HasManyAddAssociationMixin<backend_consorcio, backend_consorcioId>;
  addBackend_consorcios!: Sequelize.HasManyAddAssociationsMixin<backend_consorcio, backend_consorcioId>;
  createBackend_consorcio!: Sequelize.HasManyCreateAssociationMixin<backend_consorcio>;
  removeBackend_consorcio!: Sequelize.HasManyRemoveAssociationMixin<backend_consorcio, backend_consorcioId>;
  removeBackend_consorcios!: Sequelize.HasManyRemoveAssociationsMixin<backend_consorcio, backend_consorcioId>;
  hasBackend_consorcio!: Sequelize.HasManyHasAssociationMixin<backend_consorcio, backend_consorcioId>;
  hasBackend_consorcios!: Sequelize.HasManyHasAssociationsMixin<backend_consorcio, backend_consorcioId>;
  countBackend_consorcios!: Sequelize.HasManyCountAssociationsMixin;
  // backend_beneficiario hasMany backend_consorcio via SegundoBeneficiario_id
  SegundoBeneficiario_backend_consorcios!: backend_consorcio[];
  getSegundoBeneficiario_backend_consorcios!: Sequelize.HasManyGetAssociationsMixin<backend_consorcio>;
  setSegundoBeneficiario_backend_consorcios!: Sequelize.HasManySetAssociationsMixin<backend_consorcio, backend_consorcioId>;
  addSegundoBeneficiario_backend_consorcio!: Sequelize.HasManyAddAssociationMixin<backend_consorcio, backend_consorcioId>;
  addSegundoBeneficiario_backend_consorcios!: Sequelize.HasManyAddAssociationsMixin<backend_consorcio, backend_consorcioId>;
  createSegundoBeneficiario_backend_consorcio!: Sequelize.HasManyCreateAssociationMixin<backend_consorcio>;
  removeSegundoBeneficiario_backend_consorcio!: Sequelize.HasManyRemoveAssociationMixin<backend_consorcio, backend_consorcioId>;
  removeSegundoBeneficiario_backend_consorcios!: Sequelize.HasManyRemoveAssociationsMixin<backend_consorcio, backend_consorcioId>;
  hasSegundoBeneficiario_backend_consorcio!: Sequelize.HasManyHasAssociationMixin<backend_consorcio, backend_consorcioId>;
  hasSegundoBeneficiario_backend_consorcios!: Sequelize.HasManyHasAssociationsMixin<backend_consorcio, backend_consorcioId>;
  countSegundoBeneficiario_backend_consorcios!: Sequelize.HasManyCountAssociationsMixin;
  // backend_beneficiario hasMany backend_miembro via Beneficiario_id
  backend_miembros!: backend_miembro[];
  getBackend_miembros!: Sequelize.HasManyGetAssociationsMixin<backend_miembro>;
  setBackend_miembros!: Sequelize.HasManySetAssociationsMixin<backend_miembro, backend_miembroId>;
  addBackend_miembro!: Sequelize.HasManyAddAssociationMixin<backend_miembro, backend_miembroId>;
  addBackend_miembros!: Sequelize.HasManyAddAssociationsMixin<backend_miembro, backend_miembroId>;
  createBackend_miembro!: Sequelize.HasManyCreateAssociationMixin<backend_miembro>;
  removeBackend_miembro!: Sequelize.HasManyRemoveAssociationMixin<backend_miembro, backend_miembroId>;
  removeBackend_miembros!: Sequelize.HasManyRemoveAssociationsMixin<backend_miembro, backend_miembroId>;
  hasBackend_miembro!: Sequelize.HasManyHasAssociationMixin<backend_miembro, backend_miembroId>;
  hasBackend_miembros!: Sequelize.HasManyHasAssociationsMixin<backend_miembro, backend_miembroId>;
  countBackend_miembros!: Sequelize.HasManyCountAssociationsMixin;
  // backend_beneficiario hasMany backend_postulacion via Beneficiario_id
  backend_postulacions!: backend_postulacion[];
  getBackend_postulacions!: Sequelize.HasManyGetAssociationsMixin<backend_postulacion>;
  setBackend_postulacions!: Sequelize.HasManySetAssociationsMixin<backend_postulacion, backend_postulacionId>;
  addBackend_postulacion!: Sequelize.HasManyAddAssociationMixin<backend_postulacion, backend_postulacionId>;
  addBackend_postulacions!: Sequelize.HasManyAddAssociationsMixin<backend_postulacion, backend_postulacionId>;
  createBackend_postulacion!: Sequelize.HasManyCreateAssociationMixin<backend_postulacion>;
  removeBackend_postulacion!: Sequelize.HasManyRemoveAssociationMixin<backend_postulacion, backend_postulacionId>;
  removeBackend_postulacions!: Sequelize.HasManyRemoveAssociationsMixin<backend_postulacion, backend_postulacionId>;
  hasBackend_postulacion!: Sequelize.HasManyHasAssociationMixin<backend_postulacion, backend_postulacionId>;
  hasBackend_postulacions!: Sequelize.HasManyHasAssociationsMixin<backend_postulacion, backend_postulacionId>;
  countBackend_postulacions!: Sequelize.HasManyCountAssociationsMixin;
  // backend_beneficiario hasMany backend_proyecto via Beneficiario_id
  backend_proyectos!: backend_proyecto[];
  getBackend_proyectos!: Sequelize.HasManyGetAssociationsMixin<backend_proyecto>;
  setBackend_proyectos!: Sequelize.HasManySetAssociationsMixin<backend_proyecto, backend_proyectoId>;
  addBackend_proyecto!: Sequelize.HasManyAddAssociationMixin<backend_proyecto, backend_proyectoId>;
  addBackend_proyectos!: Sequelize.HasManyAddAssociationsMixin<backend_proyecto, backend_proyectoId>;
  createBackend_proyecto!: Sequelize.HasManyCreateAssociationMixin<backend_proyecto>;
  removeBackend_proyecto!: Sequelize.HasManyRemoveAssociationMixin<backend_proyecto, backend_proyectoId>;
  removeBackend_proyectos!: Sequelize.HasManyRemoveAssociationsMixin<backend_proyecto, backend_proyectoId>;
  hasBackend_proyecto!: Sequelize.HasManyHasAssociationMixin<backend_proyecto, backend_proyectoId>;
  hasBackend_proyectos!: Sequelize.HasManyHasAssociationsMixin<backend_proyecto, backend_proyectoId>;
  countBackend_proyectos!: Sequelize.HasManyCountAssociationsMixin;
  // backend_beneficiario belongsTo backend_ubicacion via LugarDeCreacion_id
  LugarDeCreacion!: backend_ubicacion;
  getLugarDeCreacion!: Sequelize.BelongsToGetAssociationMixin<backend_ubicacion>;
  setLugarDeCreacion!: Sequelize.BelongsToSetAssociationMixin<backend_ubicacion, backend_ubicacionId>;
  createLugarDeCreacion!: Sequelize.BelongsToCreateAssociationMixin<backend_ubicacion>;

  static initModel(sequelize: Sequelize.Sequelize): typeof backend_beneficiario {
    return backend_beneficiario.init({
    ID: {
      autoIncrement: true,
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true
    },
    Nombre: {
      type: DataTypes.STRING(100),
      allowNull: false
    },
    FechaDeCreacion: {
      type: DataTypes.DATEONLY,
      allowNull: false
    },
    TipoDePersona: {
      type: DataTypes.STRING(30),
      allowNull: false
    },
    TipoDeEmpresa: {
      type: DataTypes.STRING(30),
      allowNull: false
    },
    Perfil: {
      type: DataTypes.STRING(30),
      allowNull: false
    },
    RUTdeEmpresa: {
      type: DataTypes.STRING(12),
      allowNull: false
    },
    RUTdeRepresentante: {
      type: DataTypes.STRING(12),
      allowNull: false
    },
    LugarDeCreacion_id: {
      type: DataTypes.BIGINT,
      allowNull: false,
      references: {
        model: 'backend_ubicacion',
        key: 'ID'
      }
    }
  }, {
    sequelize,
    tableName: 'backend_beneficiario',
    timestamps: false,
    indexes: [
      {
        name: "PRIMARY",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "ID" },
        ]
      },
      {
        name: "backend_beneficiario_LugarDeCreacion_id_319c7c6a_fk_backend_u",
        using: "BTREE",
        fields: [
          { name: "LugarDeCreacion_id" },
        ]
      },
    ]
  });
  }
}
