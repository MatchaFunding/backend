import * as Sequelize from 'sequelize';
import { DataTypes, Model, Optional } from 'sequelize';
import type { backend_persona, backend_personaId } from './backend_persona';

export interface backend_usuarioAttributes {
  ID: number;
  NombreDeUsuario: string;
  Contrasena: string;
  Correo: string;
  Persona_id: number;
}

export type backend_usuarioPk = "ID";
export type backend_usuarioId = backend_usuario[backend_usuarioPk];
export type backend_usuarioOptionalAttributes = "ID";
export type backend_usuarioCreationAttributes = Optional<backend_usuarioAttributes, backend_usuarioOptionalAttributes>;

export class backend_usuario extends Model<backend_usuarioAttributes, backend_usuarioCreationAttributes> implements backend_usuarioAttributes {
  ID!: number;
  NombreDeUsuario!: string;
  Contrasena!: string;
  Correo!: string;
  Persona_id!: number;

  // backend_usuario belongsTo backend_persona via Persona_id
  Persona!: backend_persona;
  getPersona!: Sequelize.BelongsToGetAssociationMixin<backend_persona>;
  setPersona!: Sequelize.BelongsToSetAssociationMixin<backend_persona, backend_personaId>;
  createPersona!: Sequelize.BelongsToCreateAssociationMixin<backend_persona>;

  static initModel(sequelize: Sequelize.Sequelize): typeof backend_usuario {
    return backend_usuario.init({
    ID: {
      autoIncrement: true,
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true
    },
    NombreDeUsuario: {
      type: DataTypes.STRING(200),
      allowNull: false
    },
    Contrasena: {
      type: DataTypes.STRING(200),
      allowNull: false
    },
    Correo: {
      type: DataTypes.STRING(200),
      allowNull: false
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
    tableName: 'backend_usuario',
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
        name: "backend_usuario_Persona_id_0d597647_fk_backend_persona_ID",
        using: "BTREE",
        fields: [
          { name: "Persona_id" },
        ]
      },
    ]
  });
  }
}
