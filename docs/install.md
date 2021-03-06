# Installation

The fastest way of installing this package is through PyPI:

```shell
python3 -m pip install git+https://github.com/redeboer/PawianTools@master
```

This installs the latest version that you can find on the
[`master`](https://github.com/redeboer/PawianTools/tree/master) branch.

However, we highly recommend using the more dynamic,
{ref}`'editable installation' <pwa:develop:Editable installation>` instead.
This goes as follows:

1. Get the source code (see {doc}`pwa:software/git`):

   ```shell
   git clone https://github.com/redeboer/PawianTools.git
   cd PawianTools
   ```

2. **[Recommended]** Create a virtual environment (see
   {ref}`here <pwa:develop:Virtual environment>`).

3. Install the project in
   {ref}`'editable installation' <pwa:develop:Editable installation>` with
   {ref}`additional dependencies <pwa:develop:Optional dependencies>` for the
   developer:

   ```shell
   python3 -m pip install -e .[dev]
   ```

That's all! Have a look at the {doc}`/usage` page to try out the package, and
see {doc}`pwa:develop` for tips on how to work with this 'editable' developer
setup!
