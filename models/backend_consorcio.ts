import * as Sequelize from 'sequelize';
import { DataTypes, Model, Optional } from 'sequelize';
import type { backend_beneficiario, backend_beneficiarioId } from './backend_beneficiario';

export interface backend_consorcioAttributes {
  ID: number;
  PrimerBeneficiario_id: number;
  SegundoBeneficiario_id: number;
}

export type backend_consorcioPk = "ID";
export type backend_consorcioId = backend_consorcio[backend_consorcioPk];
export type backend_consorcioOptionalAttributes = "ID";
export type backend_consorcioCreationAttributes = Optional<backend_consorcioAttributes, backend_consorcioOptionalAttributes>;

export class backend_consorcio extends Model<backend_consorcioAttributes, backend_consorcioCreationAttributes> implements backend_consorcioAttributes {
  ID!: number;
  PrimerBeneficiario_id!: number;
  SegundoBeneficiario_id!: number;

  // backend_consorcio belongsTo backend_beneficiario via PrimerBeneficiario_id
  PrimerBeneficiario!: backend_beneficiario;
  getPrimerBeneficiario!: Sequelize.BelongsToGetAssociationMixin<backend_beneficiario>;
  setPrimerBeneficiario!: Sequelize.BelongsToSetAssociationMixin<backend_beneficiario, backend_beneficiarioId>;
  createPrimerBeneficiario!: Sequelize.BelongsToCreateAssociationMixin<backend_beneficiario>;
  // backend_consorcio belongsTo backend_beneficiario via SegundoBeneficiario_id
  SegundoBeneficiario!: backend_beneficiario;
  getSegundoBeneficiario!: Sequelize.BelongsToGetAssociationMixin<backend_beneficiario>;
  setSegundoBeneficiario!: Sequelize.BelongsToSetAssociationMixin<backend_beneficiario, backend_beneficiarioId>;
  createSegundoBeneficiario!: Sequelize.BelongsToCreateAssociationMixin<backend_beneficiario>;

  static initModel(sequelize: Sequelize.Sequelize): typeof backend_consorcio {
    return backend_consorcio.init({
    ID: {
      autoIncrement: true,
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true
    },
    PrimerBeneficiario_id: {
      type: DataTypes.BIGINT,
      allowNull: false,
      references: {
        model: 'backend_beneficiario',
        key: 'ID'
      }
    },
    SegundoBeneficiario_id: {
      type: DataTypes.BIGINT,
      allowNull: false,
      references: {
        model: 'backend_beneficiario',
        key: 'ID'
      }
    }
  }, {
    sequelize,
    tableName: 'backend_consorcio',
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
        name: "backend_consorcio_PrimerBeneficiario_i_b6ef7ee0_fk_backend_b",
        using: "BTREE",
        fields: [
          { name: "PrimerBeneficiario_id" },
        ]
      },
      {
        name: "backend_consorcio_SegundoBeneficiario__bdc99fa0_fk_backend_b",
        using: "BTREE",
        fields: [
          { name: "SegundoBeneficiario_id" },
        ]
      },
    ]
  });
  }
}
