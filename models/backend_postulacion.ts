import * as Sequelize from 'sequelize';
import { DataTypes, Model, Optional } from 'sequelize';
import type { backend_beneficiario, backend_beneficiarioId } from './backend_beneficiario';
import type { backend_instrumento, backend_instrumentoId } from './backend_instrumento';
import type { backend_proyecto, backend_proyectoId } from './backend_proyecto';

export interface backend_postulacionAttributes {
  ID: number;
  Resultado: string;
  MontoObtenido: number;
  FechaDePostulacion: string;
  FechaDeResultado: string;
  Detalle: string;
  Beneficiario_id: number;
  Instrumento_id: number;
  Proyecto_id: number;
}

export type backend_postulacionPk = "ID";
export type backend_postulacionId = backend_postulacion[backend_postulacionPk];
export type backend_postulacionOptionalAttributes = "ID";
export type backend_postulacionCreationAttributes = Optional<backend_postulacionAttributes, backend_postulacionOptionalAttributes>;

export class backend_postulacion extends Model<backend_postulacionAttributes, backend_postulacionCreationAttributes> implements backend_postulacionAttributes {
  ID!: number;
  Resultado!: string;
  MontoObtenido!: number;
  FechaDePostulacion!: string;
  FechaDeResultado!: string;
  Detalle!: string;
  Beneficiario_id!: number;
  Instrumento_id!: number;
  Proyecto_id!: number;

  // backend_postulacion belongsTo backend_beneficiario via Beneficiario_id
  Beneficiario!: backend_beneficiario;
  getBeneficiario!: Sequelize.BelongsToGetAssociationMixin<backend_beneficiario>;
  setBeneficiario!: Sequelize.BelongsToSetAssociationMixin<backend_beneficiario, backend_beneficiarioId>;
  createBeneficiario!: Sequelize.BelongsToCreateAssociationMixin<backend_beneficiario>;
  // backend_postulacion belongsTo backend_instrumento via Instrumento_id
  Instrumento!: backend_instrumento;
  getInstrumento!: Sequelize.BelongsToGetAssociationMixin<backend_instrumento>;
  setInstrumento!: Sequelize.BelongsToSetAssociationMixin<backend_instrumento, backend_instrumentoId>;
  createInstrumento!: Sequelize.BelongsToCreateAssociationMixin<backend_instrumento>;
  // backend_postulacion belongsTo backend_proyecto via Proyecto_id
  Proyecto!: backend_proyecto;
  getProyecto!: Sequelize.BelongsToGetAssociationMixin<backend_proyecto>;
  setProyecto!: Sequelize.BelongsToSetAssociationMixin<backend_proyecto, backend_proyectoId>;
  createProyecto!: Sequelize.BelongsToCreateAssociationMixin<backend_proyecto>;

  static initModel(sequelize: Sequelize.Sequelize): typeof backend_postulacion {
    return backend_postulacion.init({
    ID: {
      autoIncrement: true,
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true
    },
    Resultado: {
      type: DataTypes.STRING(30),
      allowNull: false
    },
    MontoObtenido: {
      type: DataTypes.INTEGER,
      allowNull: false
    },
    FechaDePostulacion: {
      type: DataTypes.DATEONLY,
      allowNull: false
    },
    FechaDeResultado: {
      type: DataTypes.DATEONLY,
      allowNull: false
    },
    Detalle: {
      type: DataTypes.STRING(1000),
      allowNull: false
    },
    Beneficiario_id: {
      type: DataTypes.BIGINT,
      allowNull: false,
      references: {
        model: 'backend_beneficiario',
        key: 'ID'
      }
    },
    Instrumento_id: {
      type: DataTypes.BIGINT,
      allowNull: false,
      references: {
        model: 'backend_instrumento',
        key: 'ID'
      }
    },
    Proyecto_id: {
      type: DataTypes.BIGINT,
      allowNull: false,
      references: {
        model: 'backend_proyecto',
        key: 'ID'
      }
    }
  }, {
    sequelize,
    tableName: 'backend_postulacion',
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
        name: "backend_postulacion_Beneficiario_id_33a8b4c0_fk_backend_b",
        using: "BTREE",
        fields: [
          { name: "Beneficiario_id" },
        ]
      },
      {
        name: "backend_postulacion_Instrumento_id_6de725d9_fk_backend_i",
        using: "BTREE",
        fields: [
          { name: "Instrumento_id" },
        ]
      },
      {
        name: "backend_postulacion_Proyecto_id_4e2b289e_fk_backend_proyecto_ID",
        using: "BTREE",
        fields: [
          { name: "Proyecto_id" },
        ]
      },
    ]
  });
  }
}
