import * as Sequelize from 'sequelize';
import { DataTypes, Model, Optional } from 'sequelize';
import type { backend_instrumento, backend_instrumentoId } from './backend_instrumento';
import type { backend_ubicacion, backend_ubicacionId } from './backend_ubicacion';

export interface backend_financiadorAttributes {
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

export type backend_financiadorPk = "ID";
export type backend_financiadorId = backend_financiador[backend_financiadorPk];
export type backend_financiadorOptionalAttributes = "ID";
export type backend_financiadorCreationAttributes = Optional<backend_financiadorAttributes, backend_financiadorOptionalAttributes>;

export class backend_financiador extends Model<backend_financiadorAttributes, backend_financiadorCreationAttributes> implements backend_financiadorAttributes {
  ID!: number;
  Nombre!: string;
  FechaDeCreacion!: string;
  TipoDePersona!: string;
  TipoDeEmpresa!: string;
  Perfil!: string;
  RUTdeEmpresa!: string;
  RUTdeRepresentante!: string;
  LugarDeCreacion_id!: number;

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
  // backend_financiador belongsTo backend_ubicacion via LugarDeCreacion_id
  LugarDeCreacion!: backend_ubicacion;
  getLugarDeCreacion!: Sequelize.BelongsToGetAssociationMixin<backend_ubicacion>;
  setLugarDeCreacion!: Sequelize.BelongsToSetAssociationMixin<backend_ubicacion, backend_ubicacionId>;
  createLugarDeCreacion!: Sequelize.BelongsToCreateAssociationMixin<backend_ubicacion>;

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
      {
        name: "backend_financiador_LugarDeCreacion_id_d8f71306_fk_backend_u",
        using: "BTREE",
        fields: [
          { name: "LugarDeCreacion_id" },
        ]
      },
    ]
  });
  }
}
