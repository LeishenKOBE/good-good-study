// 解析 url 的参数

function getUrlParams(url) {
  let reg = /([^?&=]+)=([^?&=]+)/g;
  let obj = {};
  url.replace(reg, function () {
    obj[arguments[1]] = arguments[2];
  });
}
