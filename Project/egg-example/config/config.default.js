/* eslint valid-jsdoc: "off" */

"use strict";

/**
 * @param {Egg.EggAppInfo} appInfo app info
 */
module.exports = (appInfo) => {
  /**
   * built-in config
   * @type {Egg.EggAppConfig}
   **/
  const config = (exports = {});

  // use for cookie sign key, should change to your own and keep security
  config.keys = appInfo.name + "_1652286607824_3591";

  // add your middleware config here
  config.middleware = [];
  config.security = {
    csrf: {
      enable: false,
      ignoreJSON: true,
    },
    domainWhiteList: ["*"], // 配置白名单
  };

  config.view = {
    mapping: { ".html": "ejs" }, //左边写成.html后缀，会自动渲染.html文件
  };
  exports.mysql = {
    // 单数据库信息配置
    client: {
      host: "localhost",
      port: "3306",
      user: "root",
      password: "zhaodongno1", // 初始化密码，没设置的可以不写
      database: "juejue-cost", // 我们新建的数据库名称
    },
    // 是否加载到 app 上，默认开启
    app: true,
    // 是否加载到 agent 上，默认关闭
    agent: false,
  };
  config.jwt = {
    secret: "shidongzhao",
  };

  config.multipart = {
    mode: "file",
  };
  config.cors = {
    origin: "*", // 允许所有跨域访问
    credentials: true, // 允许 Cookie 跨域跨域
    allowMethods: "GET,HEAD,PUT,POST,DELETE,PATCH",
  };

  // add your user config here
  const userConfig = {
    // myAppName: 'egg',
    uploadDir: "app/public/upload",
  };

  return {
    ...config,
    ...userConfig,
  };
};
