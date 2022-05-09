const express = require('express');
const app = express();
const PORT = process.env.PORT || 5000;
app.use(express.json());
app.get('/', (req, res) => {
    res.send("Simple API Gateway");
});
const productRoutes = require('./api/routes/products');
const stockRoutes=require('./api/routes/stocks');
const chartRoutes=require('./api/routes/charts');
app.use('/products',productRoutes);
app.use('/stocks',stockRoutes);
app.use('/charts',chartRoutes);
app.listen(PORT,()=>console.log(`Server is running at port ${PORT}`));