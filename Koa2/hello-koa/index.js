const koa = require("koa");
const Router = require("koa-router");

const app = new koa();
const router = new Router();

router.get("/", async (ctx, next) => {
  console.log(ctx, next);
  ctx.body = "Hello, world!";
});

app.use(router.routes()).use(router.allowedMethods());

const port = process.env.PORT || 3000;

app.listen(port, () => {
  console.log("Hello, world!");
});
