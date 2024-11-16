.. Nome Da Seção (H1)

Como Usar
=========

.. Ancora de direcionamento para chegar nesta página

.. _installation:

.. Subseção (H2)

Instalação
------------

Para usar, primeiro clone o repositório do projeto e instale as dependências:

.. code-block:: console

    git clone https://github.com/mauriciobenjamin700/Mini-Curso-ENUCOMPI-ERCEMAP-2024
    cd Mini-Curso-ENUCOMPI-ERCEMAP-2024
    pip install -r requirements.txt | poetry install


Creating recipes
----------------

you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError