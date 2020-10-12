class SearchRequest(object):
    def search_hotel(self):
        return """
            query searchHotel(
                $adult: Int!, 
                $filter: FilterParam, 
                $groupFilterKeyword: String, 
                $night: Int!, $page: Int!, 
                $priorityRankingType: String, 
                $room: Int!, 
                $searchType: String!, 
                $searchValue: String!, 
                $sort: String, 
                $startDate: String!
            ) {
                searchHotel(adult: $adult, filter: $filter, groupFilterKeyword: $groupFilterKeyword, night: $night, page: $page, priorityRankingType: $priorityRankingType, room: $room, searchType: $searchType, searchValue: $searchValue, sort: $sort, startDate: $startDate) 
                { 
                    code
                    message
                    errors
                    data {
                        contents {
                            id
                            name
                            address
                            postalCode
                            starRating
                            country {
                                id
                                name        
                            }   
                            region {
                                id
                                name
                            }
                            city {
                                id
                                name
                            }
                            area {
                                id
                                name
                            }
                            location {
                                coordinates {
                                    latitude
                                    longitude
                                }
                            }
                            reviews {
                                score
                                tiket {
                                    count
                                    impression
                                    rating
                                    ratingImageUrl
                                    url
                                }
                                tripadvisor {
                                    count
                                    impression
                                    rating
                                    ratingImageUrl
                                    url
                                }
                            }
                            category {
                                id
                                name
                            }
                            mainImage {
                                caption
                                url
                                mobileUrl
                            }
                            mainFacilities {
                                name
                                icon
                            }
                            poiDistance
                            itemColor
                            availableRoom
                            refundable
                            rateInfo {
                                currency
                                refundable
                                price {
                                    baseRateWithTax
                                    rateWithTax
                                    totalBaseRateWithTax
                                    totalRateWithTax
                                }
                                priceSummary {
                                    totalWithoutTax
                                    taxAndOtherFee
                                    total
                                    compulsory {
                                        text
                                        rate
                                    }
                                    pricePerNight {
                                        stayingDate
                                        rate
                                    }
                                    totalObject {
                                        label
                                        value
                                    }
                                }
                            }
                            promo {
                                promoText
                                memberDeals
                                tonightDeals
                                packageDeals
                                promoIcon
                                expiredDate
                            }
                            valueAdded
                            paymentOption
                            soldOut
                            freeWifi
                            freeBreakfast
                            isNewHotel
                            benefitAdded {
                                id
                                name
                                iconUrl
                            }
                            listAdded {
                                id
                                name
                                iconUrl
                                subName
                            }
                        }
                        pagination {
                            currentPage
                            totalData
                            totalDataInPage
                            totalPage
                        }
                        paymentOptionList {
                            description
                            disclaimer
                            icon
                            id
                            name
                            subName
                        }
                        searchDetail {
                            adult
                            checkInDate
                            checkOutDate
                            coordinates {
                                latitude
                                longitude
                            }
                            night
                            room
                            searchLocation
                        }
                    }
                }
            }
        """