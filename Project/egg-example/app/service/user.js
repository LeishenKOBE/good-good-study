//  service/user.js
"use strict";

const Service = require("egg").Service;

class UserService extends Service {
  async getUserByName(username) {
    const { app } = this;
    try {
      const result = await app.mysql.get("user", { username });
      return result;
    } catch (err) {
      console.log(err);
      return null;
    }
  }

  async register(params) {
    const { app } = this;
    try {
      const result = await app.mysql.insert("user", params);
      return result;
    } catch (err) {
      console.log(err);
      return null;
    }
  }
  async editUserInfo(params) {
    const { app, ctx } = this;
    try {
      let result = await app.mysql.update(
        "user",
        { ...params },
        {
          id: params.id, // 筛选出 id 等于 params.id 的用户
        }
      );
      return result;
    } catch (err) {
      console.log(err);
      return null;
    }
  }
}

module.exports = UserService;
