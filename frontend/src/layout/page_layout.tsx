import PageHeader from "../components/page_header";

interface PageLayoutProps {
  readonly title: string;
  readonly children: JSX.Element;
}

export default function PageLayout(props: PageLayoutProps) {
  return (
    <div id="page" className="flex flex-col w-full">
      <PageHeader title={props.title} />
      <div className="flex flex-row p-4">{props.children}</div>
    </div>
  );
}
