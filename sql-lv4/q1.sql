-- 우유와 요거트가 담긴 장바구니
SELECT a.CART_ID FROM (
    SELECT CART_ID 
    FROM CART_PRODUCTS 
    WHERE NAME in ("Milk", "Yogurt") 
    GROUP BY NAME, CART_ID
) as a 
GROUP BY a.CART_ID 
HAVING COUNT(*) >= 2