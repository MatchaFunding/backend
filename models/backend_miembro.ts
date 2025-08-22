import * as Sequelize from 'sequelize';
import { DataTypes, Model, Optional } from 'sequelize';
import type { backend_beneficiario, backend_beneficiarioId } from './backend_beneficiario';
import type { backend_persona, backend_personaId } from './backend_persona';

export interface backend_miembroAttributes {
  ID: number;
  Beneficiario_id: number;
  Persona_id: number;
}

export type backend_miembroPk = "ID";
export type backend_miembroId = backend_miembro[backend_miembroPk];
export type backend_miembroOptionalAttributes = "ID";
export type backend_miembroCreationAttributes = Optional<backend_miembroAttributes, backend_miembroOptionalAttributes>;

export class backend_miembro extends Model<backend_miembroAttributes, backend_miembroCreationAttributes> implements backend_miembroAttributes {
  ID!: number;
  Beneficiario_id!: number;
  Persona_id!: number;

  // backend_miembro belongsTo backend_beneficiario via Beneficiario_id
  Beneficiario!: backend_beneficiario;
  getBeneficiario!: Sequelize.BelongsToGetAssociationMixin<backend_beneficiario>;
  setBeneficiario!: Sequelize.BelongsToSetAssociationMixin<backend_beneficiario, backend_beneficiarioId>;
  createBeneficiario!: Sequelize.BelongsToCreateAssociationMixin<backend_beneficiario>;
  // backend_miembro belongsTo backend_persona via Persona_id
  Persona!: backend_persona;
  getPersona!: Sequelize.BelongsToGetAssociationMixin<backend_persona>;
  setPersona!: Sequelize.BelongsToSetAssociationMixin<backend_persona, backend_personaId>;
  createPersona!: Sequelize.BelongsToCreateAssociationMixin<backend_persona>;

  static initModel(sequelize: Sequelize.Sequelize): typeof backend_miembro {
    return backend_miembro.init({
    ID: {
      autoIncrement: true,
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true
    },
    Beneficiario_id: {
      type: DataTypes.BIGINT,
      allowNull: false,
      references: {
        model: 'backend_beneficiario',
        key: 'ID'
      }
    },
    Persona_id: {
      type: DataTypes.BIGINT,
      allowNull: false,
      references: {
        model: 'backend_persona',
        key: 'ID'
      }
    }
  }, {
    sequelize,
    tableName: 'backend_miembro',
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
        name: "backend_miembro_Beneficiario_id_efa3b813_fk_backend_b",
        using: "BTREE",
        fields: [
          { name: "Beneficiario_id" },
        ]
      },
      {
        name: "backend_miembro_Persona_id_1e107dcd_fk_backend_persona_ID",
        using: "BTREE",
        fields: [
          { name: "Persona_id" },
        ]
      },
    ]
  });
  }
}
