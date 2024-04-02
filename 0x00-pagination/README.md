# 0x00. Pagination (Back-end)
  

## Resources

Read or watch:

- <a href="https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination" target="_blank">REST API Design: Pagination</a>
- <a href="https://en.wikipedia.org/wiki/HATEOAS" target="_blank">HATEOAS</a>

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Requirements

- All your files will be interpreted/compiled on `Ubuntu 18.04 LTS` using `python3 (version 3.7)`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle style (version 2.5.*)`
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be `type-annotated`.

> Setup: **Popular_Baby_Names.csv**
>
> <a href="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240402%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240402T100825Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9625730366eed89de44884431cd042ce1b9bbbb7236141e8441ff244f47d8e67" target="_blank">use this data file</a> for your project. A copy is also found <a href="https://github.com/Sampul-CodeMine/alx-backend/blob/master/0x00-pagination/Popular_Baby_Names.csv">here</a>
>

---

Dukeson Ehigboria