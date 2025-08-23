import * as Sequelize from 'sequelize';
import { DataTypes, Model, Optional } from 'sequelize';
import type { auth_user_groups, auth_user_groupsId } from './auth_user_groups';
import type { auth_user_user_permissions, auth_user_user_permissionsId } from './auth_user_user_permissions';
import type { django_admin_log, django_admin_logId } from './django_admin_log';

export interface auth_userAttributes {
  id: number;
  password: string;
  last_login?: Date;
  is_superuser: number;
  username: string;
  first_name: string;
  last_name: string;
  email: string;
  is_staff: number;
  is_active: number;
  date_joined: Date;
}

export type auth_userPk = "id";
export type auth_userId = auth_user[auth_userPk];
export type auth_userOptionalAttributes = "id" | "last_login";
export type auth_userCreationAttributes = Optional<auth_userAttributes, auth_userOptionalAttributes>;

export class auth_user extends Model<auth_userAttributes, auth_userCreationAttributes> implements auth_userAttributes {
  id!: number;
  password!: string;
  last_login?: Date;
  is_superuser!: number;
  username!: string;
  first_name!: string;
  last_name!: string;
  email!: string;
  is_staff!: number;
  is_active!: number;
  date_joined!: Date;

  // auth_user hasMany auth_user_groups via user_id
  auth_user_groups!: auth_user_groups[];
  getAuth_user_groups!: Sequelize.HasManyGetAssociationsMixin<auth_user_groups>;
  setAuth_user_groups!: Sequelize.HasManySetAssociationsMixin<auth_user_groups, auth_user_groupsId>;
  addAuth_user_group!: Sequelize.HasManyAddAssociationMixin<auth_user_groups, auth_user_groupsId>;
  addAuth_user_groups!: Sequelize.HasManyAddAssociationsMixin<auth_user_groups, auth_user_groupsId>;
  createAuth_user_group!: Sequelize.HasManyCreateAssociationMixin<auth_user_groups>;
  removeAuth_user_group!: Sequelize.HasManyRemoveAssociationMixin<auth_user_groups, auth_user_groupsId>;
  removeAuth_user_groups!: Sequelize.HasManyRemoveAssociationsMixin<auth_user_groups, auth_user_groupsId>;
  hasAuth_user_group!: Sequelize.HasManyHasAssociationMixin<auth_user_groups, auth_user_groupsId>;
  hasAuth_user_groups!: Sequelize.HasManyHasAssociationsMixin<auth_user_groups, auth_user_groupsId>;
  countAuth_user_groups!: Sequelize.HasManyCountAssociationsMixin;
  // auth_user hasMany auth_user_user_permissions via user_id
  auth_user_user_permissions!: auth_user_user_permissions[];
  getAuth_user_user_permissions!: Sequelize.HasManyGetAssociationsMixin<auth_user_user_permissions>;
  setAuth_user_user_permissions!: Sequelize.HasManySetAssociationsMixin<auth_user_user_permissions, auth_user_user_permissionsId>;
  addAuth_user_user_permission!: Sequelize.HasManyAddAssociationMixin<auth_user_user_permissions, auth_user_user_permissionsId>;
  addAuth_user_user_permissions!: Sequelize.HasManyAddAssociationsMixin<auth_user_user_permissions, auth_user_user_permissionsId>;
  createAuth_user_user_permission!: Sequelize.HasManyCreateAssociationMixin<auth_user_user_permissions>;
  removeAuth_user_user_permission!: Sequelize.HasManyRemoveAssociationMixin<auth_user_user_permissions, auth_user_user_permissionsId>;
  removeAuth_user_user_permissions!: Sequelize.HasManyRemoveAssociationsMixin<auth_user_user_permissions, auth_user_user_permissionsId>;
  hasAuth_user_user_permission!: Sequelize.HasManyHasAssociationMixin<auth_user_user_permissions, auth_user_user_permissionsId>;
  hasAuth_user_user_permissions!: Sequelize.HasManyHasAssociationsMixin<auth_user_user_permissions, auth_user_user_permissionsId>;
  countAuth_user_user_permissions!: Sequelize.HasManyCountAssociationsMixin;
  // auth_user hasMany django_admin_log via user_id
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

  static initModel(sequelize: Sequelize.Sequelize): typeof auth_user {
    return auth_user.init({
    id: {
      autoIncrement: true,
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true
    },
    password: {
      type: DataTypes.STRING(128),
      allowNull: false
    },
    last_login: {
      type: DataTypes.DATE(6),
      allowNull: true
    },
    is_superuser: {
      type: DataTypes.BOOLEAN,
      allowNull: false
    },
    username: {
      type: DataTypes.STRING(150),
      allowNull: false,
      unique: "username"
    },
    first_name: {
      type: DataTypes.STRING(150),
      allowNull: false
    },
    last_name: {
      type: DataTypes.STRING(150),
      allowNull: false
    },
    email: {
      type: DataTypes.STRING(254),
      allowNull: false
    },
    is_staff: {
      type: DataTypes.BOOLEAN,
      allowNull: false
    },
    is_active: {
      type: DataTypes.BOOLEAN,
      allowNull: false
    },
    date_joined: {
      type: DataTypes.DATE(6),
      allowNull: false
    }
  }, {
    sequelize,
    tableName: 'auth_user',
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
        name: "username",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "username" },
        ]
      },
    ]
  });
  }
}
