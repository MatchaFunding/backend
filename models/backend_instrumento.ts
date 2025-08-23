import * as Sequelize from 'sequelize';
import { DataTypes, Model, Optional } from 'sequelize';
import type { backend_financiador, backend_financiadorId } from './backend_financiador';
import type { backend_postulacion, backend_postulacionId } from './backend_postulacion';

export interface backend_instrumentoAttributes {
  ID: number;
  Titulo: string;
  Alcance: string;
  Descripcion: string;
  FechaDeApertura: string;
  FechaDeCierre: string;
  DuracionEnMeses: number;
  Beneficios: string;
  Requisitos: string;
  MontoMinimo: number;
  MontoMaximo: number;
  Estado: string;
  TipoDeBeneficio: string;
  TipoDePerfil: string;
  EnlaceDelDetalle: string;
  EnlaceDeLaFoto: string;
  Financiador_id: number;
}

export type backend_instrumentoPk = "ID";
export type backend_instrumentoId = backend_instrumento[backend_instrumentoPk];
export type backend_instrumentoOptionalAttributes = "ID";
export type backend_instrumentoCreationAttributes = Optional<backend_instrumentoAttributes, backend_instrumentoOptionalAttributes>;

export class backend_instrumento extends Model<backend_instrumentoAttributes, backend_instrumentoCreationAttributes> implements backend_instrumentoAttributes {
  ID!: number;
  Titulo!: string;
  Alcance!: string;
  Descripcion!: string;
  FechaDeApertura!: string;
  FechaDeCierre!: string;
  DuracionEnMeses!: number;
  Beneficios!: string;
  Requisitos!: string;
  MontoMinimo!: number;
  MontoMaximo!: number;
  Estado!: string;
  TipoDeBeneficio!: string;
  TipoDePerfil!: string;
  EnlaceDelDetalle!: string;
  EnlaceDeLaFoto!: string;
  Financiador_id!: number;

  // backend_instrumento belongsTo backend_financiador via Financiador_id
  Financiador!: backend_financiador;
  getFinanciador!: Sequelize.BelongsToGetAssociationMixin<backend_financiador>;
  setFinanciador!: Sequelize.BelongsToSetAssociationMixin<backend_financiador, backend_financiadorId>;
  createFinanciador!: Sequelize.BelongsToCreateAssociationMixin<backend_financiador>;
  // backend_instrumento hasMany backend_postulacion via Instrumento_id
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

  static initModel(sequelize: Sequelize.Sequelize): typeof backend_instrumento {
    return backend_instrumento.init({
    ID: {
      autoIncrement: true,
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true
    },
    Titulo: {
      type: DataTypes.STRING(200),
      allowNull: false
    },
    Alcance: {
      type: DataTypes.STRING(30),
      allowNull: false
    },
    Descripcion: {
      type: DataTypes.STRING(1000),
      allowNull: false
    },
    FechaDeApertura: {
      type: DataTypes.DATEONLY,
      allowNull: false
    },
    FechaDeCierre: {
      type: DataTypes.DATEONLY,
      allowNull: false
    },
    DuracionEnMeses: {
      type: DataTypes.INTEGER,
      allowNull: false
    },
    Beneficios: {
      type: DataTypes.STRING(1000),
      allowNull: false
    },
    Requisitos: {
      type: DataTypes.STRING(1000),
      allowNull: false
    },
    MontoMinimo: {
      type: DataTypes.INTEGER,
      allowNull: false
    },
    MontoMaximo: {
      type: DataTypes.INTEGER,
      allowNull: false
    },
    Estado: {
      type: DataTypes.STRING(30),
      allowNull: false
    },
    TipoDeBeneficio: {
      type: DataTypes.STRING(30),
      allowNull: false
    },
    TipoDePerfil: {
      type: DataTypes.STRING(30),
      allowNull: false
    },
    EnlaceDelDetalle: {
      type: DataTypes.STRING(300),
      allowNull: false
    },
    EnlaceDeLaFoto: {
      type: DataTypes.STRING(300),
      allowNull: false
    },
    Financiador_id: {
      type: DataTypes.BIGINT,
      allowNull: false,
      references: {
        model: 'backend_financiador',
        key: 'ID'
      }
    }
  }, {
    sequelize,
    tableName: 'backend_instrumento',
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
        name: "backend_instrumento_Financiador_id_0b587c15_fk_backend_f",
        using: "BTREE",
        fields: [
          { name: "Financiador_id" },
        ]
      },
    ]
  });
  }
}
