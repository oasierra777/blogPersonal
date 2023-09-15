
function ServiceCard({data, index}){
    return(
        <div 
            onMouseEnter={()=>{
                const title_element = document.getElementById(index)
                title_element.classList.add('text-orange-button')
                title_element.classList.remove('text-gray-900')
            }} 
            onMouseLeave={()=>{
                const title_element = document.getElementById(index)
                title_element.classList.remove('text-orange-button')
                title_element.classList.add('text-gray-900')
            }}
            className="w-full relative p-8 h-96 lg:h-[200pm] bg-white hover:-translate-y-1 transition dutarion-300 ease-in-out">
            <div className="w-full">
                <div className="w-full">
                    {/* <i className='bx bx-code text-6xl text-gray-500' ></i> */}
                    <img src={data.img} className="w-10 h-10"/>
                    <h2 className="text-xl font-semibold text-gray-900 pt-8">{data.title}</h2>
                    <p className="text-lg font-regular text-gray-500 pt-4">{data.title}</p>
                </div>
                <div className="absolute bottom-0 left-0 p-8">
                    <h2 id={index} className="items-end text-xl font-semibold pt-8">Learn More</h2>
                </div>
            </div>
        </div>
    )
}

export default ServiceCard