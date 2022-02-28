// 数组

// let arr: Array<string> = ["122", "213312"];
// let arr1: Array<Array<string>> = [["12", "23312"], ["321312"]];
// let arr: string[][] = [["123", "123"]];

// function Arr(...args: any): void {
//   console.log(arguments);
//   let arr: IArguments = arguments;
// }

// Arr(3, 4, 5);

// 函数重载
// function fn(params: number): void;
// function fn(params: string, params2: number): void;
// function fn(params: any, params2?: any): any {
//   return params + params2;
// }

// 交叉类型
// interface Man {
//   name: string;
//   age: number;
// }

// interface People {
//   sex: string;
// }

// const getMan = (man: Man & People): void => {
//   console.log(man);
// };

// getMan({ name: "许嵩", age: 34, sex: "男" });

// 类型断言

// const fn = function (num: number | string): void {
//   console.log((num as string).length);
// };

// fn(12345);

// interface A {
//   run: string;
// }

// interface B {
//   build: string;
// }

// let fn = (type: A | B): void => {
//   console.log((<A>type).run);
// };

// let fn = (type: A | B): void => {
//   console.log((type as A).run);
// };
