"use client"
import { usePathname } from "next/navigation";
export default function notFound(){
    const patname = usePathname();
    const productId = patname.split("/")[2];
    const reviewId = patname.split("/")[4];
    return (
        <div>
            <h2>Page no Found</h2>
            Review {reviewId} not found porduct {productId}
        </div>
    );
}