import * as Sequelize from 'sequelize';
import { DataTypes, Model, Optional } from 'sequelize';
import type { auth_permission, auth_permissionId } from './auth_permission';
import type { django_admin_log, django_admin_logId } from './django_admin_log';

export interface django_content_typeAttributes {
  id: number;
  app_label: string;
  model: string;
}

export type django_content_typePk = "id";
export type django_content_typeId = django_content_type[django_content_typePk];
export type django_content_typeOptionalAttributes = "id";
export type django_content_typeCreationAttributes = Optional<django_content_typeAttributes, django_content_typeOptionalAttributes>;

export class django_content_type extends Model<django_content_typeAttributes, django_content_typeCreationAttributes> implements django_content_typeAttributes {
  id!: number;
  app_label!: string;
  model!: string;

  // django_content_type hasMany auth_permission via content_type_id
  auth_permissions!: auth_permission[];
  getAuth_permissions!: Sequelize.HasManyGetAssociationsMixin<auth_permission>;
  setAuth_permissions!: Sequelize.HasManySetAssociationsMixin<auth_permission, auth_permissionId>;
  addAuth_permission!: Sequelize.HasManyAddAssociationMixin<auth_permission, auth_permissionId>;
  addAuth_permissions!: Sequelize.HasManyAddAssociationsMixin<auth_permission, auth_permissionId>;
  createAuth_permission!: Sequelize.HasManyCreateAssociationMixin<auth_permission>;
  removeAuth_permission!: Sequelize.HasManyRemoveAssociationMixin<auth_permission, auth_permissionId>;
  removeAuth_permissions!: Sequelize.HasManyRemoveAssociationsMixin<auth_permission, auth_permissionId>;
  hasAuth_permission!: Sequelize.HasManyHasAssociationMixin<auth_permission, auth_permissionId>;
  hasAuth_permissions!: Sequelize.HasManyHasAssociationsMixin<auth_permission, auth_permissionId>;
  countAuth_permissions!: Sequelize.HasManyCountAssociationsMixin;
  // django_content_type hasMany django_admin_log via content_type_id
  django_admin_logs!: django_admin_log[];
  getDjango_admin_logs!: Sequelize.HasManyGetAssociationsMixin<django_admin_log>;
  setDjango_admin_logs!: Sequelize.HasManySetAssociationsMixin<django_admin_log, django_admin_logId>;
  addDjango_admin_log!: Sequelize.HasManyAddAssociationMixin<django_admin_log, django_admin_logId>;
  addDjango_admin_logs!: Sequelize.HasManyAddAssociationsMixin<django_admin_log, django_admin_logId>;
  createDjango_admin_log!: Sequelize.HasManyCreateAssociationMixin<django_admin_log>;
  removeDjango_admin_log!: Sequelize.HasManyRemoveAssociationMixin<django_admin_log, django_admin_logId>;
  removeDjango_admin_logs!: Sequelize.HasManyRemoveAssociationsMixin<django_admin_log, django_admin_logId>;
  hasDjango_admin_log!: Sequelize.HasManyHasAssociationMixin<django_admin_log, django_admin_logId>;
  hasDjango_admin_logs!: Sequelize.HasManyHasAssociationsMixin<django_admin_log, django_admin_logId>;
  countDjango_admin_logs!: Sequelize.HasManyCountAssociationsMixin;

  static initModel(sequelize: Sequelize.Sequelize): typeof django_content_type {
    return django_content_type.init({
    id: {
      autoIncrement: true,
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true
    },
    app_label: {
      type: DataTypes.STRING(100),
      allowNull: false
    },
    model: {
      type: DataTypes.STRING(100),
      allowNull: false
    }
  }, {
    sequelize,
    tableName: 'django_content_type',
    timestamps: false,
    indexes: [
      {
        name: "PRIMARY",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "id" },
        ]
      },
      {
        name: "django_content_type_app_label_model_76bd3d3b_uniq",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "app_label" },
          { name: "model" },
        ]
      },
    ]
  });
  }
}
