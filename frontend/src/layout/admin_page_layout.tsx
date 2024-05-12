import PageHeader from "../components/page_header";
import Navigation from "../components/navigation";

interface PageLayoutProps {
    readonly title: string;
    readonly children: JSX.Element;
}

/**
 * This component is a simple layout, which contains a navigation bar, a title and
 * all components that this component surrounds.
 *
 * Use this, if you want to create a new admin page.
 */
export default function AdminPageLayout(props: PageLayoutProps) {
    return (
        <div id="page" className="flex flex-col w-full">
            <PageHeader title={props.title} />
            <Navigation />
            <div className="flex flex-row p-4">{props.children}</div>
        </div>
    );
}
