import * as Sequelize from 'sequelize';
import { DataTypes, Model, Optional } from 'sequelize';
import type { backend_persona, backend_personaId } from './backend_persona';
import type { backend_proyecto, backend_proyectoId } from './backend_proyecto';

export interface backend_colaboradorAttributes {
  ID: number;
  Persona_id: number;
  Proyecto_id: number;
}

export type backend_colaboradorPk = "ID";
export type backend_colaboradorId = backend_colaborador[backend_colaboradorPk];
export type backend_colaboradorOptionalAttributes = "ID";
export type backend_colaboradorCreationAttributes = Optional<backend_colaboradorAttributes, backend_colaboradorOptionalAttributes>;

export class backend_colaborador extends Model<backend_colaboradorAttributes, backend_colaboradorCreationAttributes> implements backend_colaboradorAttributes {
  ID!: number;
  Persona_id!: number;
  Proyecto_id!: number;

  // backend_colaborador belongsTo backend_persona via Persona_id
  Persona!: backend_persona;
  getPersona!: Sequelize.BelongsToGetAssociationMixin<backend_persona>;
  setPersona!: Sequelize.BelongsToSetAssociationMixin<backend_persona, backend_personaId>;
  createPersona!: Sequelize.BelongsToCreateAssociationMixin<backend_persona>;
  // backend_colaborador belongsTo backend_proyecto via Proyecto_id
  Proyecto!: backend_proyecto;
  getProyecto!: Sequelize.BelongsToGetAssociationMixin<backend_proyecto>;
  setProyecto!: Sequelize.BelongsToSetAssociationMixin<backend_proyecto, backend_proyectoId>;
  createProyecto!: Sequelize.BelongsToCreateAssociationMixin<backend_proyecto>;

  static initModel(sequelize: Sequelize.Sequelize): typeof backend_colaborador {
    return backend_colaborador.init({
    ID: {
      autoIncrement: true,
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true
    },
    Persona_id: {
      type: DataTypes.BIGINT,
      allowNull: false,
      references: {
        model: 'backend_persona',
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
    tableName: 'backend_colaborador',
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
        name: "backend_colaborador_Persona_id_c406811b_fk_backend_persona_ID",
        using: "BTREE",
        fields: [
          { name: "Persona_id" },
        ]
      },
      {
        name: "backend_colaborador_Proyecto_id_4917ea19_fk_backend_proyecto_ID",
        using: "BTREE",
        fields: [
          { name: "Proyecto_id" },
        ]
      },
    ]
  });
  }
}
