import * as Sequelize from 'sequelize';
import { DataTypes, Model, Optional } from 'sequelize';
import type { backend_colaborador, backend_colaboradorId } from './backend_colaborador';
import type { backend_miembro, backend_miembroId } from './backend_miembro';
import type { backend_usuario, backend_usuarioId } from './backend_usuario';

export interface backend_personaAttributes {
  ID: number;
  Nombre: string;
  Sexo: string;
  RUT: string;
}

export type backend_personaPk = "ID";
export type backend_personaId = backend_persona[backend_personaPk];
export type backend_personaOptionalAttributes = "ID";
export type backend_personaCreationAttributes = Optional<backend_personaAttributes, backend_personaOptionalAttributes>;

export class backend_persona extends Model<backend_personaAttributes, backend_personaCreationAttributes> implements backend_personaAttributes {
  ID!: number;
  Nombre!: string;
  Sexo!: string;
  RUT!: string;

  // backend_persona hasMany backend_colaborador via Persona_id
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
  // backend_persona hasMany backend_miembro via Persona_id
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
  // backend_persona hasMany backend_usuario via Persona_id
  backend_usuarios!: backend_usuario[];
  getBackend_usuarios!: Sequelize.HasManyGetAssociationsMixin<backend_usuario>;
  setBackend_usuarios!: Sequelize.HasManySetAssociationsMixin<backend_usuario, backend_usuarioId>;
  addBackend_usuario!: Sequelize.HasManyAddAssociationMixin<backend_usuario, backend_usuarioId>;
  addBackend_usuarios!: Sequelize.HasManyAddAssociationsMixin<backend_usuario, backend_usuarioId>;
  createBackend_usuario!: Sequelize.HasManyCreateAssociationMixin<backend_usuario>;
  removeBackend_usuario!: Sequelize.HasManyRemoveAssociationMixin<backend_usuario, backend_usuarioId>;
  removeBackend_usuarios!: Sequelize.HasManyRemoveAssociationsMixin<backend_usuario, backend_usuarioId>;
  hasBackend_usuario!: Sequelize.HasManyHasAssociationMixin<backend_usuario, backend_usuarioId>;
  hasBackend_usuarios!: Sequelize.HasManyHasAssociationsMixin<backend_usuario, backend_usuarioId>;
  countBackend_usuarios!: Sequelize.HasManyCountAssociationsMixin;

  static initModel(sequelize: Sequelize.Sequelize): typeof backend_persona {
    return backend_persona.init({
    ID: {
      autoIncrement: true,
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true
    },
    Nombre: {
      type: DataTypes.STRING(200),
      allowNull: false
    },
    Sexo: {
      type: DataTypes.STRING(30),
      allowNull: false
    },
    RUT: {
      type: DataTypes.STRING(12),
      allowNull: false
    }
  }, {
    sequelize,
    tableName: 'backend_persona',
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
