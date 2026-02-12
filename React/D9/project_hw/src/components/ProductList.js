import { useEffect } from "react";
import axios from "axios";
import { useSelector, useDispatch } from "react-redux";
import { setProducts } from "../store/productSlice";
import { Link } from "react-router-dom";

function ProductList() {
  const token = useSelector(state => state.auth.token);
  const products = useSelector(state => state.products.items);
  const dispatch = useDispatch();

  useEffect(() => {
    if (products.length === 0 && token) {
      axios.get(
        "https://worksheet-product.mashupstack.com/product",
        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      ).then(res => {
        dispatch(setProducts(res.data));
      });
    }
  }, [token]);

  return (
    <div>
      <h2>Product List</h2>

      {products.map(p => (
        <div key={p.id}>
          <b>{p.name}</b>
          <Link to={`/product/${p.id}`}>
            <button>View</button>
          </Link>
          <hr/>
        </div>
      ))}
    </div>
  );
}

export default ProductList;
