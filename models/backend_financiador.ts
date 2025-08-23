import * as Sequelize from 'sequelize';
import { DataTypes, Model, Optional } from 'sequelize';
import type { backend_instrumento, backend_instrumentoId } from './backend_instrumento';

export interface backend_financiadorAttributes {
  ID: number;
  Nombre: string;
  FechaDeCreacion: string;
  RegionDeCreacion: string;
  Direccion: string;
  TipoDePersona: string;
  TipoDeEmpresa: string;
  Perfil: string;
  RUTdeEmpresa: string;
  RUTdeRepresentante: string;
}

export type backend_financiadorPk = "ID";
export type backend_financiadorId = backend_financiador[backend_financiadorPk];
export type backend_financiadorOptionalAttributes = "ID";
export type backend_financiadorCreationAttributes = Optional<backend_financiadorAttributes, backend_financiadorOptionalAttributes>;

export class backend_financiador extends Model<backend_financiadorAttributes, backend_financiadorCreationAttributes> implements backend_financiadorAttributes {
  ID!: number;
  Nombre!: string;
  FechaDeCreacion!: string;
  RegionDeCreacion!: string;
  Direccion!: string;
  TipoDePersona!: string;
  TipoDeEmpresa!: string;
  Perfil!: string;
  RUTdeEmpresa!: string;
  RUTdeRepresentante!: string;

  // backend_financiador hasMany backend_instrumento via Financiador_id
  backend_instrumentos!: backend_instrumento[];
  getBackend_instrumentos!: Sequelize.HasManyGetAssociationsMixin<backend_instrumento>;
  setBackend_instrumentos!: Sequelize.HasManySetAssociationsMixin<backend_instrumento, backend_instrumentoId>;
  addBackend_instrumento!: Sequelize.HasManyAddAssociationMixin<backend_instrumento, backend_instrumentoId>;
  addBackend_instrumentos!: Sequelize.HasManyAddAssociationsMixin<backend_instrumento, backend_instrumentoId>;
  createBackend_instrumento!: Sequelize.HasManyCreateAssociationMixin<backend_instrumento>;
  removeBackend_instrumento!: Sequelize.HasManyRemoveAssociationMixin<backend_instrumento, backend_instrumentoId>;
  removeBackend_instrumentos!: Sequelize.HasManyRemoveAssociationsMixin<backend_instrumento, backend_instrumentoId>;
  hasBackend_instrumento!: Sequelize.HasManyHasAssociationMixin<backend_instrumento, backend_instrumentoId>;
  hasBackend_instrumentos!: Sequelize.HasManyHasAssociationsMixin<backend_instrumento, backend_instrumentoId>;
  countBackend_instrumentos!: Sequelize.HasManyCountAssociationsMixin;

  static initModel(sequelize: Sequelize.Sequelize): typeof backend_financiador {
    return backend_financiador.init({
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
    RegionDeCreacion: {
      type: DataTypes.STRING(30),
      allowNull: false
    },
    Direccion: {
      type: DataTypes.STRING(300),
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
    }
  }, {
    sequelize,
    tableName: 'backend_financiador',
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
    ]
  });
  }
}
