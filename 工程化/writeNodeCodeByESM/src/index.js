import { add } from "./utils.js";
import { readFileSync } from "fs";

const json = readFileSync("./package.json");
const info = JSON.parse(json);

console.log(add(1, 2));
