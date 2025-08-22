import * as Sequelize from 'sequelize';
import { DataTypes, Model, Optional } from 'sequelize';
import type { backend_beneficiario, backend_beneficiarioId } from './backend_beneficiario';
import type { backend_financiador, backend_financiadorId } from './backend_financiador';
import type { backend_instrumento, backend_instrumentoId } from './backend_instrumento';
import type { backend_proyecto, backend_proyectoId } from './backend_proyecto';

export interface backend_ubicacionAttributes {
  ID: number;
  Region: string;
  Capital: string;
  Calle: string;
  Numero: number;
}

export type backend_ubicacionPk = "ID";
export type backend_ubicacionId = backend_ubicacion[backend_ubicacionPk];
export type backend_ubicacionOptionalAttributes = "ID";
export type backend_ubicacionCreationAttributes = Optional<backend_ubicacionAttributes, backend_ubicacionOptionalAttributes>;

export class backend_ubicacion extends Model<backend_ubicacionAttributes, backend_ubicacionCreationAttributes> implements backend_ubicacionAttributes {
  ID!: number;
  Region!: string;
  Capital!: string;
  Calle!: string;
  Numero!: number;

  // backend_ubicacion hasMany backend_beneficiario via LugarDeCreacion_id
  backend_beneficiarios!: backend_beneficiario[];
  getBackend_beneficiarios!: Sequelize.HasManyGetAssociationsMixin<backend_beneficiario>;
  setBackend_beneficiarios!: Sequelize.HasManySetAssociationsMixin<backend_beneficiario, backend_beneficiarioId>;
  addBackend_beneficiario!: Sequelize.HasManyAddAssociationMixin<backend_beneficiario, backend_beneficiarioId>;
  addBackend_beneficiarios!: Sequelize.HasManyAddAssociationsMixin<backend_beneficiario, backend_beneficiarioId>;
  createBackend_beneficiario!: Sequelize.HasManyCreateAssociationMixin<backend_beneficiario>;
  removeBackend_beneficiario!: Sequelize.HasManyRemoveAssociationMixin<backend_beneficiario, backend_beneficiarioId>;
  removeBackend_beneficiarios!: Sequelize.HasManyRemoveAssociationsMixin<backend_beneficiario, backend_beneficiarioId>;
  hasBackend_beneficiario!: Sequelize.HasManyHasAssociationMixin<backend_beneficiario, backend_beneficiarioId>;
  hasBackend_beneficiarios!: Sequelize.HasManyHasAssociationsMixin<backend_beneficiario, backend_beneficiarioId>;
  countBackend_beneficiarios!: Sequelize.HasManyCountAssociationsMixin;
  // backend_ubicacion hasMany backend_financiador via LugarDeCreacion_id
  backend_financiadors!: backend_financiador[];
  getBackend_financiadors!: Sequelize.HasManyGetAssociationsMixin<backend_financiador>;
  setBackend_financiadors!: Sequelize.HasManySetAssociationsMixin<backend_financiador, backend_financiadorId>;
  addBackend_financiador!: Sequelize.HasManyAddAssociationMixin<backend_financiador, backend_financiadorId>;
  addBackend_financiadors!: Sequelize.HasManyAddAssociationsMixin<backend_financiador, backend_financiadorId>;
  createBackend_financiador!: Sequelize.HasManyCreateAssociationMixin<backend_financiador>;
  removeBackend_financiador!: Sequelize.HasManyRemoveAssociationMixin<backend_financiador, backend_financiadorId>;
  removeBackend_financiadors!: Sequelize.HasManyRemoveAssociationsMixin<backend_financiador, backend_financiadorId>;
  hasBackend_financiador!: Sequelize.HasManyHasAssociationMixin<backend_financiador, backend_financiadorId>;
  hasBackend_financiadors!: Sequelize.HasManyHasAssociationsMixin<backend_financiador, backend_financiadorId>;
  countBackend_financiadors!: Sequelize.HasManyCountAssociationsMixin;
  // backend_ubicacion hasMany backend_instrumento via Alcance_id
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
  // backend_ubicacion hasMany backend_proyecto via Alcance_id
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

  static initModel(sequelize: Sequelize.Sequelize): typeof backend_ubicacion {
    return backend_ubicacion.init({
    ID: {
      autoIncrement: true,
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true
    },
    Region: {
      type: DataTypes.STRING(30),
      allowNull: false
    },
    Capital: {
      type: DataTypes.STRING(30),
      allowNull: false
    },
    Calle: {
      type: DataTypes.STRING(300),
      allowNull: false
    },
    Numero: {
      type: DataTypes.INTEGER,
      allowNull: false
    }
  }, {
    sequelize,
    tableName: 'backend_ubicacion',
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
