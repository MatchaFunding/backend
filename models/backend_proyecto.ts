import * as Sequelize from 'sequelize';
import { DataTypes, Model, Optional } from 'sequelize';
import type { backend_beneficiario, backend_beneficiarioId } from './backend_beneficiario';
import type { backend_colaborador, backend_colaboradorId } from './backend_colaborador';
import type { backend_postulacion, backend_postulacionId } from './backend_postulacion';

export interface backend_proyectoAttributes {
  ID: number;
  Titulo: string;
  Descripcion: string;
  DuracionEnMesesMinimo: number;
  DuracionEnMesesMaximo: number;
  Alcance: string;
  Area: string;
  Beneficiario_id: number;
}

export type backend_proyectoPk = "ID";
export type backend_proyectoId = backend_proyecto[backend_proyectoPk];
export type backend_proyectoOptionalAttributes = "ID";
export type backend_proyectoCreationAttributes = Optional<backend_proyectoAttributes, backend_proyectoOptionalAttributes>;

export class backend_proyecto extends Model<backend_proyectoAttributes, backend_proyectoCreationAttributes> implements backend_proyectoAttributes {
  ID!: number;
  Titulo!: string;
  Descripcion!: string;
  DuracionEnMesesMinimo!: number;
  DuracionEnMesesMaximo!: number;
  Alcance!: string;
  Area!: string;
  Beneficiario_id!: number;

  // backend_proyecto belongsTo backend_beneficiario via Beneficiario_id
  Beneficiario!: backend_beneficiario;
  getBeneficiario!: Sequelize.BelongsToGetAssociationMixin<backend_beneficiario>;
  setBeneficiario!: Sequelize.BelongsToSetAssociationMixin<backend_beneficiario, backend_beneficiarioId>;
  createBeneficiario!: Sequelize.BelongsToCreateAssociationMixin<backend_beneficiario>;
  // backend_proyecto hasMany backend_colaborador via Proyecto_id
  backend_colaboradors!: backend_colaborador[];
  getBackend_colaboradors!: Sequelize.HasManyGetAssociationsMixin<backend_colaborador>;
  setBackend_colaboradors!: Sequelize.HasManySetAssociationsMixin<backend_colaborador, backend_colaboradorId>;
  addBackend_colaborador!: Sequelize.HasManyAddAssociationMixin<backend_colaborador, backend_colaboradorId>;
  addBackend_colaboradors!: Sequelize.HasManyAddAssociationsMixin<backend_colaborador, backend_colaboradorId>;
  createBackend_colaborador!: Sequelize.HasManyCreateAssociationMixin<backend_colaborador>;
  removeBackend_colaborador!: Sequelize.HasManyRemoveAssociationMixin<backend_colaborador, backend_colaboradorId>;
  removeBackend_colaboradors!: Sequelize.HasManyRemoveAssociationsMixin<backend_colaborador, backend_colaboradorId>;
  hasBackend_colaborador!: Sequelize.HasManyHasAssociationMixin<backend_colaborador, backend_colaboradorId>;
  hasBackend_colaboradors!: Sequelize.HasManyHasAssociationsMixin<backend_colaborador, backend_colaboradorId>;
  countBackend_colaboradors!: Sequelize.HasManyCountAssociationsMixin;
  // backend_proyecto hasMany backend_postulacion via Proyecto_id
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

  static initModel(sequelize: Sequelize.Sequelize): typeof backend_proyecto {
    return backend_proyecto.init({
    ID: {
      autoIncrement: true,
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true
    },
    Titulo: {
      type: DataTypes.STRING(300),
      allowNull: false
    },
    Descripcion: {
      type: DataTypes.STRING(500),
      allowNull: false
    },
    DuracionEnMesesMinimo: {
      type: DataTypes.INTEGER,
      allowNull: false
    },
    DuracionEnMesesMaximo: {
      type: DataTypes.INTEGER,
      allowNull: false
    },
    Alcance: {
      type: DataTypes.STRING(30),
      allowNull: false
    },
    Area: {
      type: DataTypes.STRING(100),
      allowNull: false
    },
    Beneficiario_id: {
      type: DataTypes.BIGINT,
      allowNull: false,
      references: {
        model: 'backend_beneficiario',
        key: 'ID'
      }
    }
  }, {
    sequelize,
    tableName: 'backend_proyecto',
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
        name: "backend_proyecto_Beneficiario_id_83f3b5bc_fk_backend_b",
        using: "BTREE",
        fields: [
          { name: "Beneficiario_id" },
        ]
      },
    ]
  });
  }
}
